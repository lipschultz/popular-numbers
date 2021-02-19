import json
import math
import random
import re
import sys

# from popularity import numeric_tools
from popularity.numeric_tools import *


class NumberCollection:
    def contains(self, number):
        raise NotImplementedError


class YoutubeVideo(NumberCollection):
    def __init__(self, *, raw_test, test, title, link, host, date, source, init, oeis, wiki, note):
        self.raw_test = raw_test
        self.test = test
        self.link = link
        self.title = title
        self.host = host
        self.date = date
        self.source = source
        self.init = init
        self.oeis = oeis
        self.wiki = wiki
        self.note = note

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in self.test)
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False

    def __str__(self):
        return f'<{self.title!r}@{self.link!r}>'

    def __repr__(self):
        if isinstance(self.raw_test, str):
            return str(self) + "{test : " + repr(self.raw_test.encode("unicode-escape")) + "}"
        else:
            return str(self) + "{test : " + repr(self.raw_test) + "}"

    @classmethod
    def from_json_dict(cls, json_data):
        raw_test = json_data.get('test')
        link = json_data.get('link')
        title = json_data.get('title')
        host = json_data.get('host')
        date = json_data.get('date')
        source = json_data.get('source')
        init = json_data.get('init')
        note = json_data.get('note')
        oeis = json_data.get('oeis')
        wiki = json_data.get('wiki')

        if not isinstance(raw_test, list):
            raw_test = [raw_test]
        test = []
        for t in raw_test:
            try:
                t = eval(t)
            except Exception as ex:
                print('problem evaluating test for ', title, link)
                print(t)
                print(type(ex), ex)
                print()
                t = lambda *args: False
            test.append(t)

        try:
            init = compile(init, '<json_string>', "exec")
            print("eval result for", title, ":", eval(init, globals(), locals()))
        except Exception:
            pass

        return cls(raw_test=raw_test, test=test, title=title, link=link, host=host, date=date, source=source, init=init, oeis=oeis, wiki=wiki, note=note)

    @classmethod
    def load_file(cls, filename):
        with open(filename, 'rb') as fp:
            contents = json.load(fp)

        return [cls.from_json_dict(d) for d in contents] + [MagicSquare()]


class MagicSquare(YoutubeVideo):
    """
    Creates a magic square out of the result.
    """

    def __init__(self):
        self.host = 'Matt Parker'
        self.date = 'Apr 19, 2016'
        self.weight = 1

        self.link = 'https://www.youtube.com/watch?v=aQxCnmhqZko'
        self.title = 'Magic Square Party Trick'
        self.source = 'Numberphile'

        self.oeis = None
        self.wiki = None
        self.init = None

        self.__coeff = 1 / (4 * math.sqrt(3))
        self.__exp = math.pi * math.sqrt(2 / 3)

    def contains(self, number):
        """
        Returns True if the magic square fact applies for the given result.
        """
        return is_int(number) and 21 <= number <= 65

    # def message(self, formula, result, context):
    #     """
    #     The message to display if the fact applies to the current context.
    #     """
    #     row1 = [result - 20, 1, 12, 7]
    #     row2 = [11, 8, result - 21, 2]
    #     row3 = [5, 10, 3, result - 18]
    #     row4 = [4, result - 19, 6, 9]
    #     square = [row1, row2, row3, row4]
    #     return 'The magic square for %d is %s' % (result, square)


class OEISSequence(NumberCollection):
    def __init__(self, a_number, numbers):
        self.a_number = a_number
        self.numbers = numbers

    def contains(self, number):
        return number in self.numbers

    @classmethod
    def load_file(cls, filename):
        with open(filename) as fp:
            contents = fp.readlines()

        cases = []
        for line in contents:
            if line.startswith('#'):
                continue

            a_number, *seq = line.strip().split(',')
            a_number = a_number.strip()
            seq = [int(n) for n in seq if len(n) > 0]
            cases.append(cls(a_number, seq))

        return cases
