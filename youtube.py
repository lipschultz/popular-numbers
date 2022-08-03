import math
import random
import re
import sys
from fractions import Fraction

from popularity.load import NumberCollection
from popularity.numeric_tools import *


def farey_addition(context):
    if len(context['result']) < 3 or any(not is_rational(r) for r in context['result'][-3:]):
        return False
    first = Fraction(context['result'][-3]).limit_denominator(234)
    second = Fraction(context['result'][-2]).limit_denominator(234)
    third = Fraction(context['result'][-1]).limit_denominator(234)
    return Fraction(first.numerator + third.numerator, first.denominator + third.denominator) == second


def int_to_digits(result, as_type=int):
    if as_type == int:
        return [result // 10**i % 10 for i in range(math.ceil(math.log(result, 10)))]
    else:
        return list(str(result))

def vampire(result=1260):
    digits = int_to_digits(result, str)
    result_size = len(digits)
    partition_template = [1]*(result_size//2) + [0]*(result_size//2)
    partitions = set([v for v in itertools.permutations(partition_template)])
    for p in partitions:
        f1 = int(''.join(itertools.compress(digits, p)))
        f2 = int(''.join(itertools.compress(digits, [-1*v+1 for v in p])))
        print(f1, '*', f2, '=', f1*f2, '?=', result)
        if f1*f2 == result:
            return True
    return False



class Youtube0(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SyJlRUBoVp0'
        self.title = 'The Prime Problem with a One Sentence Proof'
        self.host = ['Matthias Kreck']
        self.date = '2016-07-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result) and (result - 1) % 4 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube1(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2JM2oImb9Qg'
        self.title = '5040 and other Anti-Prime Numbers'
        self.host = ['James Grime']
        self.date = '2016-07-06'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A002182'
        self.wiki = 'https://en.wikipedia.org/wiki/Highly_composite_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1,2,4,6,12,24,36,48,60,120,180,240,360,720,840,1260,1680,2520,5040,7560,10080,15120,20160,25200,27720,45360,50400,55440,83160,110880,166320,221760,277200,332640,498960,554400,665280,720720,1081080,1441440,2162160)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube2(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AOMQxLrCI7A'
        self.title = "Speed Solve of a Rubik's Cube in Slow Motion"
        self.host = ['Ryan Jones']
        self.date = '2016-07-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (20, 479001600, 43252003274489856000)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube3(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mPn2AdMH7UQ'
        self.title = 'Surreal Numbers (writing the first book)'
        self.host = ['Donald Knuth']
        self.date = '2016-06-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Surreal_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_surreal(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube4(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5Mf0JpTI_gg'
        self.title = 'Three Gears are Possible'
        self.host = ['Henry Segerman']
        self.date = '2016-06-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result == 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube5(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5Mf0JpTI_gg'
        self.title = 'Three Gears are Possible'
        self.host = ['Henry Segerman']
        self.date = '2016-06-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result == 19])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube6(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SDw2Pu0-H4g'
        self.title = 'Consecutive Coin Flips'
        self.host = ['James Grime']
        self.date = '2016-06-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result in (4, 6)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube7(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_-M_3oV75Lw'
        self.title = '74 is cracked'
        self.host = ['Tim Browning']
        self.date = '2016-05-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result == 74])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube8(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AEpQ8YxupfQ'
        self.title = 'Money Catching'
        self.host = ['Tadashi Tokieda']
        self.date = '2016-05-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0.2])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube9(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=y12Tt3bOmKA'
        self.title = "Let's Talk About Sets"
        self.host = ['Bobby Wilson']
        self.date = '2016-05-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 0.6309297535714574, 1e-5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube10(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=YVvfY_lFUZ8'
        self.title = 'The Last Digit of Prime Numbers'
        self.host = ['James Grime']
        self.date = '2016-05-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'pairs of consecutive prime numbers'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result) and result % 10 in (1, 3, 7, 9)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube11(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VTveQ1ndH1c'
        self.title = 'The Key to the Riemann Hypothesis'
        self.host = ['Jon Keating']
        self.date = '2016-05-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0 or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube12(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VTveQ1ndH1c'
        self.title = 'The Key to the Riemann Hypothesis'
        self.host = ['Jon Keating']
        self.date = '2016-05-10'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000594'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643, -115920, 534612, -370944, -577738, 401856, 1217160, 987136, -6905934, 2727432, 10661420, -7109760, -4219488, -12830688, 18643272, 21288960, -25499225, 13865712, -73279080, 24647168)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube13(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NjCIq58rZ8I'
        self.title = 'Partitions'
        self.host = ['James Grime']
        self.date = '2016-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 10 in (4, 9)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube14(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NjCIq58rZ8I'
        self.title = 'Partitions'
        self.host = ['James Grime']
        self.date = '2016-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0  and (result-5) % 7 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube15(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NjCIq58rZ8I'
        self.title = 'Partitions'
        self.host = ['James Grime']
        self.date = '2016-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0  and (result-6) % 11 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube16(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NjCIq58rZ8I'
        self.title = 'Partitions'
        self.host = ['James Grime']
        self.date = '2016-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and (result-237) % 17303 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube17(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NjCIq58rZ8I'
        self.title = 'Partitions'
        self.host = ['James Grime']
        self.date = '2016-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and (result-2623) % 206839 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube18(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NjCIq58rZ8I'
        self.title = 'Partitions'
        self.host = ['James Grime']
        self.date = '2016-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and (result-1977147619) % 815655 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube19(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NjCIq58rZ8I'
        self.title = 'Partitions'
        self.host = ['James Grime']
        self.date = '2016-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube20(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aOT_bG-vWyg'
        self.title = 'The Parker Square'
        self.host = ['Matt Parker']
        self.date = '2016-04-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result) or result in {3051, 4107}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube21(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=eAjMvpRMVDw'
        self.title = 'Crank Files'
        self.host = ['Matt Parker', 'Brady Haran', 'Keith Moore']
        self.date = '2016-03-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube22(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4izjrtR8Ozg'
        self.title = 'Little Fibs'
        self.host = ['Colm Mulcahy']
        self.date = '2016-06-02'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A000045'
        self.wiki = 'https://en.wikipedia.org/wiki/Fibonacci_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube23(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2s4TqVAbfz4'
        self.title = 'Perfect Shapes in Higher Dimensions'
        self.host = ['Carlo Séquin']
        self.date = '2016-03-23'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A060296'
        self.wiki = 'https://en.wikipedia.org/wiki/Regular_polytope'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (1, 1, math.inf, 5, 6, 3, 3, 3, 3, 3))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube24(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WYsP1PhoAZc'
        self.title = 'Shuffling Card Trick'
        self.host = ['Jason Davison']
        self.date = '2016-03-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '%' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube25(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lEvXcTYqtKU'
        self.title = "How they found the World's Biggest Prime Number"
        self.host = ['Matt Parker']
        self.date = '2016-01-21'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A000032', 'https://oeis.org/A003010']
        self.wiki = ['https://en.wikipedia.org/wiki/Lucas_number', 'https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test']
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], LUCAS_NUMBERS[1:]) or (is_int(result) and 0 < result < len(LUCAS_NUMBERS)-1 and ((LUCAS_NUMBERS[int(result)]-1) % result == 0)) or '%' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube26(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=tlpYjrbujG0'
        self.title = "New World's Biggest Prime Number (PRINTED FULLY ON PAPER)"
        self.host = ['Matt Parker']
        self.date = '2016-01-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 74207281])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube27(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3BR8tK-LuB0'
        self.title = 'Fantastic Quaternions'
        self.host = ['James Grime']
        self.date = '2016-01-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'quaternions'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: isinstance(result, complex)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube28(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xRpR1rmPbJE'
        self.title = 'The iPhone of Slide Rules'
        self.host = ['Alex Bellos']
        self.date = '2016-01-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'slide rules'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'log' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube29(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HPfAnX5blO0'
        self.title = 'Glitch Primes and Cyclops Numbers'
        self.host = ['Simon Pampena']
        self.date = '2015-12-07'
        self.source = 'Numberphile'
        self.oeis = ['http://oeis.org/A265383', 'http://oeis.org/A138148']
        self.wiki = 'https://en.wikipedia.org/wiki/Repdigit'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (result in {1, 6, 9, 154, 253, 1114, 1390, 2618, 5611, 12871, 15286, 108609, 132574} or result in (9, ) or result in {0b0, 0b101, 0b11011, 0b1110111, 0b111101111, 0b11111011111, 0b1111110111111, 0b111111101111111, 0b11111111011111111, 0b1111111110111111111, 0b111111111101111111111, 0b11111111111011111111111} or all(v==str(result%10) for v in str(result)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube30(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wymmCdLdPvM'
        self.title = 'The Uncracked Problem with 33'
        self.host = ['Tim Browning']
        self.date = '2015-11-06'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A156638', 'https://oeis.org/A060464']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and ((result - 4) % 9 == 0 or (result - 5) % 9 == 0 or result == 33)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube31(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Lihh_lMmcDw'
        self.title = "Skewes' Massive Number"
        self.host = ['James Grime']
        self.date = '2015-10-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and result > 2])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube32(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pKwsPBeSiOc'
        self.title = 'Powers of 2'
        self.host = ['Dmitry Kleinbock']
        self.date = '2015-10-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and result > 0 and math.log(result, 2) % 1 == 0) or (is_rational(result) and result in {30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046})])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube33(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=d0vY0CKYhPY'
        self.title = 'Pi and the Mandelbrot Set'
        self.host = ['Holly Krieger']
        self.date = '2015-10-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and (result == 0.25 or is_close(math.pi, result, 1e-3) or result in {2, 30, 312, 3140, 31414})])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube34(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vA2cdHLKYB8'
        self.title = 'Philosophy of Numbers'
        self.host = ['Mark Jago']
        self.date = '2015-09-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_number(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube35(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=UTCScjoPymA'
        self.title = 'Stars and Bars (and bagels)'
        self.host = ['Ken Ribet']
        self.date = '2016-07-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'combinatorial: has_combinatorial_function'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube36(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WYijIV5JrKg'
        self.title = 'The Opposite of Infinity'
        self.host = ['James Grime']
        self.date = '2015-09-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'infinitesimal'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and result < sys.float_info.radix**sys.float_info.min_exp])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube37(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BBp0bEczCNg'
        self.title = 'The Infinitesimal Monad'
        self.host = ['Carol Wood']
        self.date = '2015-09-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and (result < sys.float_info.radix**sys.float_info.min_exp or result == math.inf)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube38(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bN8PE3eljdA'
        self.title = "What's special about 196?"
        self.host = ['James Grime']
        self.date = '2015-08-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'Lychrel Numbers'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result in {89, 196, 295, 394, 493, 592, 689, 691}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube39(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=jPcBU0Z2Hj8'
        self.title = 'The 8 Queen Problem'
        self.host = ['James Grime']
        self.date = '2015-08-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result in {8, 4426165368, 92, 12}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube40(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aqyyhhnGraw'
        self.title = 'What is a Knot?'
        self.host = ['Carlo Séquin']
        self.date = '2015-08-03'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A002863'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (0, 0, 1, 1, 2, 3, 7, 21, 49, 165, 552, 2176, 9988, 46972, 253293, 1388705))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube41(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fjEB_wbemQA'
        self.title = 'The Curse of Lane 8'
        self.host = ['Richard Tapia']
        self.date = '2015-08-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {8, 13, 14} or any([is_subsequence_of(context['result'][-3:], s) for s in ((1,7,6), (3,7,6), (2,4,7), (4,5,7), (3,8,2), (2,8,4), (4,5,4), (5,1,5), (5,1,8), (1,3,8), (6,3,5), (6,2,1), (7,6,1), (7,6,3), (8,2,3), (8,4,2))])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube42(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Km024eldY1A'
        self.title = 'How many chess games are possible?'
        self.host = ['James Grime']
        self.date = '2015-07-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "Shannon's number: 10^120; Hardy's estimate: 10^(10^50)"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 11800 or is_close(result, 147808829414345923316083210206383297601)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube43(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=99stb2mzspI'
        self.title = 'Why 1980 was a great year to be born... but 2184 will be better'
        self.host = ['Matt Parker']
        self.date = '2015-06-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1980, 45, 2025, 1892, 44, 1936, 2070, 46, 2116, 2162, 47, 2209, 2046, 2, 2048, 2184, 3, 2187, 13, 2197}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube44(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2g3sdzgSABM'
        self.title = 'Hunt for the Elusive 4th Klein Bottle'
        self.host = ['Carlo Séquin']
        self.date = '2015-06-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 4])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube45(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AAsICMPwGPY'
        self.title = 'Klein Bottles'
        self.host = ['Cliff Stoll']
        self.date = '2015-06-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0 and formula.count('-') == 1 and all([is_rational(t) and float(t) == int(float(t)) == 1 for t in formula.split('-')])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube46(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LNS1fabDkeA'
        self.title = 'Why 82,000 is an extraordinary number'
        self.host = ['James Grime']
        self.date = '2015-06-12'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A258107'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (2, 3, 4, 82000))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube47(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0hlvhQZIOQw'
        self.title = 'Funny Fractions and Ford Circles'
        self.host = ['Francis Bonahon']
        self.date = '2015-06-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "function doesn't exist!"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: farey_addition(context)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube48(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=zDJKFcZ0Kkg'
        self.title = 'More Hyperbolic Sports'
        self.host = ['Dick Canary']
        self.date = '2015-05-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'sinh' in formula or 'π' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube49(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=u6Got0X41pY'
        self.title = 'Playing Sports in Hyperbolic Space'
        self.host = ['Dick Canary']
        self.date = '2015-05-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'sinh' in formula or 'π' in formula or 'cosh' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube50(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=gjVDqfUhXOY'
        self.title = 'Billionaire Mathematician'
        self.host = ['James Harris Simons', 'Brady Haran']
        self.date = '2015-05-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {14e9, 7}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube51(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=U9qU20VmvaU'
        self.title = 'Monkeys and Coconuts'
        self.host = ['Tony Padilla']
        self.date = '2015-04-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3121, 1024, 15625, 11529, 15621} or is_close(result, 0.32768)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube52(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PnW5IRvgvLY'
        self.title = 'Ditching the Fifth Axiom'
        self.host = ['Caleb Ashley']
        self.date = '2015-04-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 5])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube53(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Y2lXsxmBx7E'
        self.title = '52-Card Perfect Shuffles'
        self.host = ['Jason Davison']
        self.date = '2015-03-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'binary numbers'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 52])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube54(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AxJubaijQbI'
        self.title = 'The Best (and Worst) Ways to Shuffle Cards'
        self.host = ['Persi Diaconis']
        self.date = '2015-03-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {7, 10000, 52} or is_close(result, 4.538) or is_close(result, 8.55)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube55(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AqcVsShxzw8'
        self.title = '1 to 200 on Google Image Search'
        self.host = []
        self.date = '2015-03-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1 <= result <= 200])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube56(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=siawhQBRC8I'
        self.title = 'Paper Calculator'
        self.host = ['Jason Shiga']
        self.date = '2016-07-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: formula in ('0+1', '0+0', '1+1')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube57(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Sa9jLWKrX0c'
        self.title = "Penney's Game"
        self.host = ['James Grime']
        self.date = '2016-07-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'combinatorics'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {7/8, 3/4, 2/3}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube58(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MEyIppEOQTw'
        self.title = 'The Electric Slide Rule'
        self.host = ['Cliff Stoll']
        self.date = '2016-08-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(f in formula for f in ('log', '*', '/'))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube59(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l4bmZ1gRqCc'
        self.title = '58 and other Confusing Numbers'
        self.host = ['Tom Scott']
        self.date = '2015-03-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'bases and number representations (+in other languages)'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {58, 771216, 1e5, 1e7, 1e12}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube60(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_qvp9a1x2UM'
        self.title = 'The Useless Number'
        self.host = ['Barry Mazur']
        self.date = '2015-02-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0 or isinstance(result, complex) or is_close(result, 5+(-15)**.5) or is_close(result, 5-(-15)**.5) or is_close(result, (-15)**.5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube61(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nUN4NDVIfVI'
        self.title = "The Bridges to Fermat's Last Theorem"
        self.host = ['Ken Ribet']
        self.date = '2015-03-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'Pythagorean Triples'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube62(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9TAlEVDvXgw'
        self.title = "Little Professor (Dr Grime's Toy Story)"
        self.host = ['James Grime']
        self.date = '2015-02-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '*' in formula or result in {624, 144}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube63(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ovsYv-b-wWI'
        self.title = 'Calculator Unboxing #7 (Gaxio)'
        self.host = ['Matt Parker']
        self.date = '2016-07-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_rational(result) and (any([is_close(result, v, 1e-7) for v in (1.411213562, 31.11269837, math.pi, (17)**.5)]) or result in (17, 8, 888))) or (is_error(result) and result.msg == 'divide by zero')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube64(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8Nzi1h2m7pE'
        self.title = 'Calculator Unboxing #6 (Staples collection)'
        self.host = ['Matt Parker']
        self.date = '2016-02-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_error(result) and result.msg == 'divide by zero') or (any(is_close(result, v, 1e-7) for v in (0.9999997, 1.9999998, 4.9999992)) or result in (40, 24089, 30, 39.9))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube65(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZbKYmfjMPVM'
        self.title = 'Calculator Unboxing #5 (Little Professor)'
        self.host = ['Matt Parker']
        self.date = '2015-02-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (8000, 13, 14, 9, 4, 788, 901, 17) or (is_real(result) and 6 <= result <= 11) or formula in ('8+5', '7+7', '5+4', '4+0', '715+73', '844+57') or is_close(result, 2.83333333333, 1e-7)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube66(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=87uo2TPrsl8'
        self.title = 'The Amazing Heptadecagon (17-gon)'
        self.host = ['David Eisenbud']
        self.date = '2015-02-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (3, 4, 5, 6, 15, 30, 60, 17, 21)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube67(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=GznQgTdEdI4'
        self.title = 'Super Egg'
        self.host = ['Alex Bellos']
        self.date = '2015-02-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 2.5])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube68(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Obg7JPd6cmw'
        self.title = 'Should you catch a tossed coin?'
        self.host = ['Persi Diaconis']
        self.date = '2015-02-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'randomness'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube69(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AYnJv68T3MM'
        self.title = 'How random is a coin toss?'
        self.host = ['Persi Diaconis']
        self.date = '2015-01-30'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'randomness'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_rational(result) and is_close(result, 0.51, 1e-3)) or is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube70(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yfr3BIk6KFc'
        self.title = 'Something special about 399 (and 2015)'
        self.host = ['Ed Copeland']
        self.date = '2015-01-15'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A006972'
        self.wiki = 'https://en.wikipedia.org/wiki/Lucas%E2%80%93Carmichael_number'
        self.note = 'maybe calculate these instead'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (399, 935, 2015, 2915, 4991, 5719, 7055, 8855, 12719, 18095, 20705, 20999, 22847, 29315, 31535, 46079, 51359, 60059, 63503, 67199, 73535, 76751, 80189, 81719, 88559, 90287, 104663, 117215, 120581, 147455, 152279, 155819, 162687, 191807, 194327, 196559, 214199, 218735, 230159, 265895, 357599, 388079, 390335, 482143, 588455, 653939, 663679, 676799, 709019, 741311, 760655, 761039, 776567, 798215, 880319, 895679, 913031, 966239, 966779, 973559, 1010735, 1017359, 1097459, 1162349, 1241099, 1256759, 1525499, 1554119, 1584599, 1587599, 1659119, 1707839, 1710863, 1719119, 1811687, 1901735, 1915199, 1965599, 2048255, 2055095, 2150819, 2193119, 2249999, 2276351, 2416679, 2581319, 2647679, 2756159, 2924099, 3106799, 3228119, 3235967, 3332999, 3354695, 3419999, 3441239, 3479111, 3483479, 3700619, 3704399, 3741479, 4107455, 4285439, 4452839, 4587839, 4681247, 4853759, 4874639, 5058719, 5455799, 5669279, 5807759, 6023039, 6514199, 6539819, 6656399, 6730559, 6959699, 6994259, 7110179, 7127999, 7234163, 7274249, 7366463, 8159759, 8164079, 8421335, 8699459, 8734109, 9224279, 9349919, 9486399, 9572639, 9694079, 9868715)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube71(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=q8n15q1v4Xo'
        self.title = 'Perfect Number Proof'
        self.host = ['Matt Parker']
        self.date = '2015-01-06'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000396'
        self.wiki = 'https://en.wikipedia.org/wiki/Perfect_number'
        self.note = 'maybe calculate these instead'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176, 191561942608236107294793378084303638130997321548169216)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube72(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=T0xKHwQH-4I'
        self.title = 'Perfect Numbers and Mersenne Primes'
        self.host = ['Matt Parker']
        self.date = '2015-01-06'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A000396', 'https://oeis.org/A000043']
        self.wiki = ['https://en.wikipedia.org/wiki/Perfect_number', 'https://en.wikipedia.org/wiki/Mersenne_prime']
        self.note = 'maybe calculate these instead'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176, 191561942608236107294793378084303638130997321548169216) or result in (2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657) or result in (3, 7, 31, 127, 8191, 131071, 524287, 2147483647, 2305843009213693951, 618970019642690137449562111, 162259276829213363391578010288127, 170141183460469231731687303715884105727)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube73(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=v678Em6qyzk'
        self.title = 'Wrong Turn on the Dragon'
        self.host = ['Donald Knuth']
        self.date = '2014-12-30'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube74(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6Lm9EHhbJAY'
        self.title = "Euclid's Big Problem"
        self.host = ['Zsuzsanna Dancso']
        self.date = '2014-12-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'something is raised to the third power'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0.5 or any(is_close(result, v, 1e-9) for v in (2**.5, 1/3, ))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube75(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SL2lYcggGpc'
        self.title = 'How to Trisect an Angle with Origami'
        self.host = ['Zsuzsanna Dancso']
        self.date = '2014-12-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 1/3, 1e-9)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube76(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=DpwUVExX27E'
        self.title = 'Infinite Fractions'
        self.host = ['Matt Parker']
        self.date = '2014-12-02'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A002487'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3, 8, 5, 7, 2, 7, 5, 8, 3, 7, 4, 5, 1, 6, 5, 9, 4, 11, 7, 10, 3, 11, 8, 13, 5, 12, 7, 9, 2, 9, 7, 12, 5, 13, 8, 11, 3, 10, 7, 11, 4, 9, 5, 6, 1, 7, 6, 11, 5, 14, 9, 13, 4, 15, 11, 18, 7, 17, 10, 13, 3, 14, 11, 19, 8, 21, 13, 18, 5, 17, 12, 19)) or is_subsequence_of(context['result'][-3:], (1/1, 1/2, 2/1, 1/3, 3/2, 2/3, 3/1, 1/4, 4/3, 3/5, 5/2, 2/5, 5/3, 3/4, 4/1))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube77(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=izdZPx89ph4'
        self.title = 'Imaginary Erdős Number'
        self.host = ['Ron Graham']
        self.date = '2014-11-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: isinstance(result, complex)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube78(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=E-d9mgo8FGk'
        self.title = 'Sum of Natural Numbers (second proof and extra footage)'
        self.host = ['Ed Copeland', 'Tony Padilla']
        self.date = '2015-01-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (-1/12, math.inf, 1/4, 26)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube79(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mX0NB9IyYpU'
        self.title = 'Math and Movies (Animation at Pixar)'
        self.host = ['Tony DeRose']
        self.date = '2014-11-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(len(context['result']) >= len(s) and context['result'][-len(s):] == s for s in ((1, 1), (1, 2, 1), (1, 3, 3, 1), (1, 4, 1)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube80(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Yajonhixy4g'
        self.title = 'All Triangles are Equilateral'
        self.host = ['Carlo Séquin']
        self.date = '2014-11-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube81(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Lsu2dIr_c8k'
        self.title = 'Leyland Numbers'
        self.host = ['Ed Copeland']
        self.date = '2014-10-28'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A076980'
        self.wiki = 'https://en.wikipedia.org/wiki/Leyland_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (8, 17, 32, 54, 57, 100, 145, 177, 320, 368, 512, 593, 945, 1124, 1649, 2169, 2530, 4240, 5392, 6250, 7073, 8361, 16580, 18785, 20412, 23401, 32993, 60049, 65792, 69632, 93312, 94932, 131361, 178478, 262468, 268705, 397585, 423393, 524649, 533169)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube82(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Lsu2dIr_c8k'
        self.title = 'Leyland Numbers'
        self.host = ['Ed Copeland']
        self.date = '2014-10-28'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A094133'
        self.wiki = 'https://en.wikipedia.org/wiki/Leyland_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (17, 593, 32993, 2097593, 8589935681, 59604644783353249, 523347633027360537213687137, 43143988327398957279342419750374600193, 4318114567396436564035293097707729426477458833, 5052785737795758503064406447721934417290878968063369478337)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube83(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=99Welatppzk'
        self.title = 'The Making of a Mile of Pi'
        self.host = ['Brady Haran', 'Hugh McPartlan', 'Torben Dam Jensen', 'Jesper Hyldager', 'Jon Kenny', 'Matt Parker', 'Sue McPartlan', 'Pete McPartlan', 'Dave Pentelow', 'Scott Pentelow', 'Josh Pentelow', 'Jacob Bateson', 'CGP Grey']
        self.date = '2014-10-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1e6, 2, 11492, 14522, 5613487, 250000, 4157, 1) or is_close(result, (66666.8, 1.052, 1.69, math.pi)) or any(is_subsequence_of(context['result'][-3:], s) for s in ((4, 8, 0, 0, 0, 4, 4, 8, 0, 0, 2), (1, 5, 6, 5, 5, 1, 5, 6, 5, 6, 6, 6, 1, 1, 1), (3, 15, 18, 15, 20), (13, 1, 20, 20), (25, 14, 8, 5, 23, 15, 8, 12, 2), (3, 1, 4, 1, 5, 9)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube84(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0r3cEKZiLmg'
        self.title = 'Mile of Pi'
        self.host = ['Brady Haran', 'Hugh McPartlan', 'Torben Dam Jensen', 'Jesper Hyldager', 'Jon Kenny', 'Matt Parker', 'Sue McPartlan', 'Pete McPartlan', 'Dave Pentelow', 'Scott Pentelow', 'Josh Pentelow', 'Jacob Bateson', 'CGP Grey']
        self.date = '2014-10-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1e6, 8, 762, 999999, 3333333, 216176, 456789, 500000, 2, 4, 100000, 996482, 5) or is_close(result, (1/15, math.pi))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube85(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PeUbRXnbmms'
        self.title = 'Lucas Numbers'
        self.host = ['Matt Parker']
        self.date = '2014-09-22'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A000045', 'https://oeis.org/A000032']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS) or is_subsequence_of(context['result'][-3:], LUCAS_NUMBERS) or (is_rational(result) and is_close(result, GOLDEN_RATIO))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube86(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=D8ntDpBm6Ok'
        self.title = 'Brady Numbers'
        self.host = ['Matt Parker']
        self.date = '2014-09-22'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A000045', 'https://oeis.org/A247698']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS) or is_subsequence_of(context['result'][-3:], (2308, 4261, 6569, 10830, 17399, 28229, 45628, 73857, 119485, 193342, 312827, 506169, 818996, 1325165, 2144161, 3469326, 5613487, 9082813, 14696300, 23779113, 38475413, 62254526, 100729939, 162984465, 263714404, 426698869, 690413273, 1117112142, 1807525415, 2924637557, 4732162972, 7656800529)) or (is_rational(result) and is_close(result, GOLDEN_RATIO)) or (len(context['result']) >= 2 and is_rational(context['result'][-2]) and is_rational(context['result'][-1]) and context['result'][-2] != 0 and is_close(context['result'][-1]/context['result'][-2], GOLDEN_RATIO, 1e-3))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube87(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dTWKKvlZB08'
        self.title = 'Golden Proof'
        self.host = ['Matt Parker']
        self.date = '2014-09-22'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000045'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS) or (is_rational(result) and is_close(result, GOLDEN_RATIO)) or (len(context['result']) >= 2 and is_rational(context['result'][-2]) and is_rational(context['result'][-1]) and context['result'][-2] != 0 and is_close(context['result'][-1]/context['result'][-2], GOLDEN_RATIO, 1e-3)) or (len(context['result']) >= 3 and all(is_rational(v) for v in context['result'][-3:]) and context['result'][-3]+context['result'][-2] == context['result'][-1])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube88(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=m5evLoL0xwg'
        self.title = 'The Three Square Geometry Problem'
        self.host = ['Zvezdelina Stankova']
        self.date = '2014-09-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (45, 26, 18, 89, 91.3, 90)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube89(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5mFpVDpKX70'
        self.title = 'UNCRACKABLE? The Collatz Conjecture'
        self.host = ['David Eisenbud']
        self.date = '2016-08-08'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A177729', 'https://oeis.org/A060412', 'https://oeis.org/A061641']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 6, 3, 9, 28, 14, 63728127, 949) or '3*Ans+1' in formula or '2*Ans' in formula or result in (1, 2, 3, 6, 7, 9, 12, 15, 18, 19, 21, 24, 25, 27, 30, 33, 36, 37, 39, 42, 43, 45, 48, 51, 54, 55, 57, 60, 63, 66, 69, 72, 73, 75, 78, 79, 81, 84, 87, 90, 93, 96, 97, 99, 102, 105, 108, 109, 111, 114, 115, 117, 120, 123, 126, 127, 129, 132, 133, 135, 138, 141) or result in (2, 3, 7, 27, 703, 10087, 35655, 270271, 362343, 381727, 626331, 1027431, 1126015, 8088063, 13421671, 20638335, 26716671, 56924955, 63728127, 217740015, 1200991791, 1827397567, 2788008987, 12235060455) or result in (0, 1, 3, 6, 7, 9, 12, 15, 18, 19, 21, 24, 25, 27, 30, 33, 36, 37, 39, 42, 43, 45, 48, 51, 54, 55, 57, 60, 63, 66, 69, 72, 73, 75, 78, 79, 81, 84, 87, 90, 93, 96, 97, 99, 102, 105, 108, 109, 111, 114, 115, 117, 120, 123, 126, 127, 129, 132, 133, 135, 138, 141, 144, 145)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube90(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=I7v2wAXFQpc'
        self.title = 'Friedman Numbers'
        self.host = ['Ed Copeland']
        self.date = '2014-09-12'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A036057', 'https://oeis.org/A080035']
        self.wiki = 'https://en.wikipedia.org/wiki/Friedman_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (25, 121, 125, 126, 127, 128, 153, 216, 289, 343, 347, 625, 688, 736, 1022, 1024, 1206, 1255, 1260, 1285, 1296, 1395, 1435, 1503, 1530, 1792, 1827, 2048, 2187, 2349, 2500, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2592 ,2737, 2916, 3125, 3159, 3281, 3375, 3378, 3685, 3784, 3864, 3972, 4088, 4096, 4106, 4167, 4536, 4624, 4628, 5120, 5776, 5832, 6144, 6145, 6455, 6880, 7928, 8092, 8192, 9025, 9216, 9261, 11264, 11664, 12850, 13825, 14641, 15552, 15585, 15612, 15613, 15617, 15618, 15621, 15622, 15623, 15624, 15626, 15632, 15633, 15642, 15645, 15655, 15656, 15662, 15667, 15688, 16377, 16384, 16447, 16875, 17536, 18432, 19453, 19683, 19739, 10192, 8326197504, 99999999, 11111111111, 123456789, 987654321, 268435179, 8, 28, 46, 78, 98)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube91(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OEMA6jhi5Qo'
        self.title = 'Wobbly Circles'
        self.host = ['Matt Parker']
        self.date = '2014-09-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (2**.5, 1-1/(2**.5)), 1e-7)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube92(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HuKl3XuEmj4'
        self.title = 'Dice Bucket'
        self.host = ['Matt Parker']
        self.date = '2014-09-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1584])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube93(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Qcv1IqHWAzg'
        self.title = 'Stable Marriage Problem'
        self.host = ['Emily Riehl']
        self.date = '2014-09-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1962])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube94(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZkVSRwFWjy0'
        self.title = 'Magic Hexagon'
        self.host = ['James Grime']
        self.date = '2014-08-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 38 or result == 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube95(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OuF-WB7mD6k'
        self.title = 'Fix a Wobbly Table (with Math)'
        self.host = ['Matthias Kreck']
        self.date = '2014-08-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and 0 <= result <= 0.25])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube96(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4UgZ5FqdYIQ'
        self.title = 'Strong Law of Small Numbers'
        self.host = ['Tony Padilla']
        self.date = '2014-08-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (3, 5, 17, 257, 65537, 4294967297, 31, 331, 3331, 33331, 333331, 3333331, 33333331, 333333331)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube97(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VDYzSzDaHuM'
        self.title = 'Can a number be boring? (feat 14972)'
        self.host = ['Tony Padilla']
        self.date = '2014-08-11'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A046704'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (14972, 17087, 23, 1121, 2121)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube98(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ea7lJkEhytA'
        self.title = 'Look-and-Say Numbers (feat John Conway)'
        self.host = ['John Conway']
        self.date = '2014-08-08'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A005150'
        self.wiki = 'https://en.wikipedia.org/wiki/Look-and-say_sequence'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221, 13211311123113112211, 11131221133112132113212221, 3113112221232112111312211312113211, 1321132132111213122112311311222113111221131221, 11131221131211131231121113112221121321132132211331222113112211, 311311222113111231131112132112311321322112111312211312111322212311322113212221) or (is_rational(result) and is_close(result, 1.303577269))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube99(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=eZUa5k_VIZg'
        self.title = 'What do 5, 13 and 563 have in common?'
        self.host = ['James Grime']
        self.date = '2014-08-03'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A007540'
        self.wiki = 'https://en.wikipedia.org/wiki/Wilson_prime'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (5, 13, 563)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube100(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=txajrEOTkuY'
        self.title = "Graham's Number Escalates Quickly"
        self.host = ['Brady Haran']
        self.date = '2014-07-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and (result in {27, 7625597484987} or (result > sys.float_info.max))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube101(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NGMRB4O922I'
        self.title = 'The Mandelbrot Set'
        self.host = ['Holly Krieger']
        self.date = '2014-07-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Mandelbrot_set'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: isinstance(result, complex) or (is_rational(result) and 0 < result <= 2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube102(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HX8bihEe3nA'
        self.title = "What is Graham's Number? (feat Ron Graham)"
        self.host = ['Ron Graham']
        self.date = '2014-07-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result >= 13])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube103(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=shEk8sz1oOw'
        self.title = 'Fundamental Theorem of Algebra'
        self.host = ['David Eisenbud']
        self.date = '2014-07-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: isinstance(result, complex)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube104(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xPk3SZiFEvQ'
        self.title = 'Happy Ending Problem'
        self.host = ['Ron Graham']
        self.date = '2014-07-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube105(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZWib5olGbQ0'
        self.title = 'Mathematical Way to Choose a Toilet'
        self.host = ['Ria Symonds']
        self.date = '2014-06-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and is_close(result, (36.7879, 0.367879))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube106(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sxLdGjV-_yg'
        self.title = 'Calculator Unboxing #4 (Bamboo Calculator)'
        self.host = ['Matt Parker']
        self.date = '2014-06-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 0.11111111111, 1e-11) or result == 0 or (is_error(result) and result.msg == 'divide by zero') or result in {23, 21}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube107(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xdiL-ADRTxQ'
        self.title = 'Friends and Strangers Theorem'
        self.host = ['Simon Pampena']
        self.date = '2014-06-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 6])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube108(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8l-La9HEUIU'
        self.title = 'Odd Equations'
        self.host = ['David Eisenbud']
        self.date = '2014-06-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 2 == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube109(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7u6kFlWZOWg'
        self.title = 'Monty Hall Problem for Dummies'
        self.host = ['Brady Haran']
        self.date = '2014-05-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3 or is_close(result, (1/3, 2/3), 1e-7)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube110(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4Lb-6rxZxx0'
        self.title = 'Monty Hall Problem'
        self.host = ['Lisa Goldberg']
        self.date = '2014-05-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3 or is_close(result, (1/3, 2/3), 1e-7)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube111(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Nyo3TjKyu_c'
        self.title = 'How many panels on a soccer ball?'
        self.host = ['Teena Gerhardt']
        self.date = '2014-05-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 12, 20}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube112(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xOCe5HUObD4'
        self.title = 'Life, Death and the Monster'
        self.host = ['John Conway']
        self.date = '2014-05-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {808017424794512875886459904961710757005754368000000000, 83155536130867200003, 196883}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube113(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=jsSeoGpiWsw'
        self.title = 'Monster Group'
        self.host = ['John Conway', 'Tim Burness']
        self.date = '2014-05-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {26, 808017424794512875886459904961710757005754368000000000, 196883}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube114(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=00Qu1kgsGpM'
        self.title = 'Professors React to 2048'
        self.host = ['Laurence Eaves', 'Martyn Poliakoff', 'Phil Moriarty', 'Ed Copeland', 'Tony Padilla']
        self.date = '2014-05-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 3228}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube115(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CwIAfkuXc5A'
        self.title = 'Order from Chaos'
        self.host = ['Simon Pampena']
        self.date = '2014-04-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {362880, 1764}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube116(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=GItmC9lxeco'
        self.title = 'Poincaré Conjecture'
        self.host = ['Katie Steckles', 'James Isenberg']
        self.date = '2014-04-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2002, 4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube117(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sG_6nlMZ8f4'
        self.title = 'Epic Circles'
        self.host = ['Simon Pampena']
        self.date = '2014-04-13'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A242412'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, [1/v for v in (15, 23, 39, 63, 95, 135, 183, 239, 303, 375, 455, 543, 639, 743, 855, 975, 1103, 1239, 1383, 1535, 1695, 1863, 2039, 2223, 2415, 2615, 2823, 3039, 3263, 3495, 3735, 3983, 4239, 4503, 4775, 5055, 5343, 5639, 5943, 6255, 6575, 6903, 7239, 7583, 7935, 8295, 8663, 9039, 9423, 9815)], 1e-9)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube118(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lNuPy-r1GuQ'
        self.title = 'Domino Addition'
        self.host = ['Matt Parker']
        self.date = '2014-04-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '+' in formula or result == 59 or result == 82])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube119(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3T7jMcstxY0'
        self.title = 'The Greatest Ever Infographic'
        self.host = ['James Grime']
        self.date = '2014-04-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1812, 127000, 100000, 50000, 28000, -21, 60000, 33000, 422000, 10000)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube120(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7dcDuVyzb8Y'
        self.title = 'Measuring Coastline'
        self.host = ['Steve Mould']
        self.date = '2014-03-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (9, 22, 3, 4, 0, math.inf)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube121(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=09JslnY7W_k'
        self.title = '63 and -7/4 are special'
        self.host = ['Holly Krieger']
        self.date = '2014-03-24'
        self.source = 'Numberphile'
        self.oeis = ['http://oeis.org/A000225', 'http://oeis.org/A003095']
        self.wiki = None
        self.note = 'exact formula given -- should adjust it to be more forgiving, also any formula of form Ans**2+c (c is Integer, c != 0, -1, -2) is acceptable'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647, 4294967295) or result in (0, 1, 2, 5, 26, 677, 458330, 210066388901, 44127887745906175987802, 1947270476915296449559703445493848930452791205, 3791862310265926082868235028027893277370233152247388584761734150717768254410341175325352026) or result == -7/4 or isinstance(result, complex) or formula in ('2*Ans+1', 'Ans**2+1') or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube122(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0Oazb7IWzbA'
        self.title = 'Why -1/12 is a gold nugget'
        self.host = ['Edward Frenkel']
        self.date = '2014-03-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (math.inf, 0) or is_close(result, (-1/12, 1/120), 1e-9)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube123(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=TUErNWBOkUM'
        self.title = 'Pi me a River'
        self.host = ['James Grime']
        self.date = '2014-03-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.pi])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube124(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=E36qMxXGo3A'
        self.title = 'Pi Prog Rock'
        self.host = ['Alan Stewart']
        self.date = '2014-03-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (311, 157) or is_close(result, (math.pi, 22/8, 7/9, math.pi/4, 2*math.pi)) or context['result'][-50:] == PI_DIGITS[:50]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube125(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=d6c6uIyieoo'
        self.title = 'Riemann Hypothesis'
        self.host = ['Edward Frenkel']
        self.date = '2014-03-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.pi**2/6, 1.202056903159594, -1/12)) or isinstance(result, complex) or result in {1, -1, 1/2} or (is_int(result) and result < 0 and result % 2 == 0) or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube126(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OAss481FfAQ'
        self.title = 'Brussels Sprouts'
        self.host = ['Teena Gerhardt']
        self.date = '2014-03-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 2])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube127(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OAss481FfAQ'
        self.title = 'Brussels Sprouts'
        self.host = ['Teena Gerhardt']
        self.date = '2014-03-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 2])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube128(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=E8kUJL04ELA'
        self.title = 'Does John Conway hate his Game of Life?'
        self.host = ['John Conway']
        self.date = '2014-03-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (2, 3)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube129(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vzV50goW_WM'
        self.title = 'Log Tables (extra bit)'
        self.host = ['Roger Bowley']
        self.date = '2014-03-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (0.9895192582062144, 0.367879422971105), 1e-9) or 'log' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube130(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=y8acoaakvPM'
        self.title = 'Fifth Root Trick'
        self.host = ['Simon Pampena']
        self.date = '2014-02-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 10 <= result <= 99])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube131(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=y8acoaakvPM'
        self.title = 'Fifth Root Trick'
        self.host = ['Simon Pampena']
        self.date = '2014-02-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 10 <= result <= 99])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube132(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=jbiaz_aHHUQ'
        self.title = 'Liar Numbers'
        self.host = ['James Grime']
        self.date = '2014-02-03'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A002997'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube133(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HvMSRWTE2mI'
        self.title = 'Fool-Proof Test for Primes'
        self.host = ['James Grime']
        self.date = '2014-02-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube134(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Yexc19j3TjE'
        self.title = 'Why do people hate mathematics?'
        self.host = ['Edward Frenkel']
        self.date = '2014-01-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: True])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube135(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ab_dY3dZFHM'
        self.title = "Knight's Tour"
        self.host = ['Brady Haran']
        self.date = '2014-01-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {26534728821064, 64, 260, 520, 130, 210, 282, 140}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube136(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=w-I6XTVZXww'
        self.title = 'ASTOUNDING: 1 + 2 + 3 + 4 + 5 + ... = -1/12'
        self.host = ['Tony Padilla', 'Ed Copeland']
        self.date = '2014-01-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {-1/12, 1/2, 1/4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube137(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NPoj8lk9Fo4'
        self.title = 'Pi is Beautiful'
        self.host = ['James Grime']
        self.date = '2014-01-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi, 1e-11)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube138(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wyl-V0mrEio'
        self.title = 'Calculator Unboxing #3 (Casio Watch)'
        self.host = ['Matt Parker']
        self.date = '2013-12-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: formula in {'7*0.1428572', '1/0'} or is_close(result, (1.0000004, 0.9999999), 1e-7) or result in {40, math.inf}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube139(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6aDBGTWsydY'
        self.title = 'Calculator Unboxing #2 (Casio fx)'
        self.host = ['Matt Parker']
        self.date = '2013-12-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: formula in {'1/9', '17^(1/2)', '17^0.5', '17^.5'} or result in {1/9, 17**.5, 55.5}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube140(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1O69uBL22nY'
        self.title = 'NSA Surveillance (an extra bit)'
        self.host = ['Edward Frenkel']
        self.date = '2013-12-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'random'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube141(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qbkH_0TNdk0'
        self.title = 'More about Pebbling a Chessboard'
        self.host = ['Zvezdelina Stankova']
        self.date = '2013-12-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 4])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube142(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ulg_AHBOIQU'
        self.title = 'How did the NSA hack our emails?'
        self.host = ['Edward Frenkel']
        self.date = '2013-12-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'mod' in formula or result in PRIME_NUMBERS[1000:] or result in {115792089210356248762697446949407573530086143415290314195533631308867097853951, 115792089210356248762697446949407573530086143415290314195533631, 115792089210356248762697446949407573529996955224135760342422259061068512044369, 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b, 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5, 0xc49d360886e704936a6678e1139d26b7819f7e90, 0x7efba1662985be9403cb055c75d4f7e0ce8d84a9c5114abcaf3177680104fa0d}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube143(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lFQGSGsXbXE'
        self.title = 'Pebbling a Chessboard'
        self.host = ['Zvezdelina Stankova']
        self.date = '2013-12-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {math.inf, 2}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube144(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yDWPi1pZ0Po'
        self.title = 'Connect Four'
        self.host = ['Brady Haran']
        self.date = '2013-12-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4, 4531985219092, 2626652048471, 1905333170621, 7, 728, 713298878, 41}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube145(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kOClr_bew38'
        self.title = '10:10 in Watch Advertisements'
        self.host = []
        self.date = '2013-12-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 10])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube146(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bJDiZi9dqOg'
        self.title = '87,539,319'
        self.host = ['Simon Singh']
        self.date = '2013-11-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {87539319, 1729, 6963472309248}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube147(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=K305Vu7hFg0'
        self.title = 'Pi and Four Fingers'
        self.host = ['Simon Singh']
        self.date = '2013-10-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.pi**4/90, 3.11037552421026430215)) or result == math.pi])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube148(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WUlaUalgxqI'
        self.title = 'Cyclic Numbers'
        self.host = ['Tony Padilla']
        self.date = '2013-10-27'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A001913'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 588235294117647, lambda formula, result, context: result in {7, 17, 19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 167, 179, 181, 193, 223, 229, 233, 257, 263, 269, 313, 337, 367, 379, 383, 389, 419, 433, 461, 487, 491, 499, 503, 509, 541, 571, 577, 593, 619, 647, 659, 701, 709, 727, 743, 811, 821, 823, 857, 863, 887, 937, 941, 953, 971, 977, 983}, lambda formula, result, context: (is_int(result) and result % 7 == 0), lambda formula, result, context: result in ((10**(p-1)-1)/p for p in (7, 17, 19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 167, 179, 181, 193, 223, 229, 233, 257, 263, 269, 313, 337, 367, 379, 383, 389, 419, 433, 461, 487, 491, 499, 503, 509, 541, 571, 577, 593, 619, 647, 659, 701, 709, 727, 743, 811, 821, 823, 857, 863, 887, 937, 941, 953, 971, 977, 983)), lambda formula, result, context: is_close(result, 37.395)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube149(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_YysNM2JoFo'
        self.title = "Sloane's Gap"
        self.host = ['James Grime']
        self.date = '2013-10-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube150(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=eaJtjJNrWf0'
        self.title = 'Calculator Unboxing #1'
        self.host = ['Matt Parker']
        self.date = '2013-10-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(result == v for v in (1.9999998, 1e-5, 1.99999999999, 0.99999999999)) or (is_error(result) and result.msg == 'divide by zero') or result in {25, 2, 41, 27} or formula == '5+2*5'])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube151(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ReOQ300AcSU'
        self.title = 'Homer Simpson vs Pierre de Fermat'
        self.host = ['Simon Singh']
        self.date = '2013-09-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3987, 12, 4365, 4472, 1782, 1841, 1922}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube152(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CfoKor05k1I'
        self.title = 'Politics and Numbers'
        self.host = ['James Grime']
        self.date = '2013-10-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {223, 75, 107, 21} or (is_real(result) and 40 <= result < 50)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube153(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qiNcEguuFSA'
        self.title = "Fermat's Last Theorem"
        self.host = ['Simon Singh']
        self.date = '2013-09-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube154(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Y30VF3cSIYQ'
        self.title = 'The Legend of Question Six'
        self.host = ['Simon Pampena']
        self.date = '2016-08-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 6 or (is_int(result) and result > 0 and result**0.5 % 1 == 0)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube155(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Nu-lW-Ifyec'
        self.title = 'Fibonacci Mystery'
        self.host = ['James Grime']
        self.date = '2013-09-18'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A001175'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS) or is_subsequence_of(context['result'][-3:], (0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1)) or is_subsequence_of(context['result'][-3:], (1, 3, 8, 6, 20, 24, 16, 12, 24, 60, 10, 24, 28, 48, 40, 24, 36, 24, 18, 60, 16, 30, 48, 24, 100, 84, 72, 48, 14, 120, 30, 48, 40, 36, 80, 24, 76, 18, 56, 60, 40, 48, 88, 30, 120, 48, 32, 24, 112, 300, 72, 84, 108, 72, 20, 48, 72, 42, 58, 120, 60, 30, 48, 96, 140, 120, 136))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube156(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VRzH4xB0GdM'
        self.title = 'Log Tables'
        self.host = ['Roger Bowley']
        self.date = '2013-09-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'log' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube157(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8UqCyepX3AI'
        self.title = 'WARNING: Contains Numbers'
        self.host = ['James Grime']
        self.date = '2013-09-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'prime number list needs to include 6-digit primes'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result < 1e7 and (is_prime(result) or result == 492113)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube158(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kCSzjExvbTQ'
        self.title = 'Phone Buttons'
        self.host = ['Sarah Wiseman']
        self.date = '2013-08-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result <= 9])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube159(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=N7BABxMlOs0'
        self.title = 'Can Fish Count?'
        self.host = ['Brian Butterworth']
        self.date = '2013-08-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result <= 7])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube160(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xEpLW_I21jY'
        self.title = 'Brady just talks about whatever'
        self.host = ['Brady Haran']
        self.date = '2013-08-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and (500000 <= result or result == 14)) or is_close(result, (math.e, math.pi))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube161(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l8ezziaEeNE'
        self.title = 'Primes are like Weeds (PNT)'
        self.host = ['James Grime']
        self.date = '2013-08-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube162(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l8ezziaEeNE'
        self.title = 'Primes are like Weeds (PNT)'
        self.host = ['James Grime']
        self.date = '2013-08-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube163(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aIggWlKr41w'
        self.title = 'Point about Points'
        self.host = ['Simon Pampena']
        self.date = '2013-08-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_irrational(result) or result == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube164(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=YBbBbY4qvv4'
        self.title = 'British Numbers confuse Americans'
        self.host = ['CGP Grey', 'Lynne Murphy']
        self.date = '2013-07-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(str(i)*2 in str(result) for i in range(0, 10)) or (is_rational(result) and 1100 <= result <= 9999) or context['result'][-3:] == [1, 2, 3] or result == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube165(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6ltrPVPEwfo'
        self.title = 'Awesome Prime Number Constant'
        self.host = ['James Grime']
        self.date = '2013-07-18'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A051021', 'https://oeis.org/A051254']
        self.wiki = 'https://en.wikipedia.org/wiki/Mills%27_constant'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 1.30637788386308069, 1e-17) or result in {2, 11, 1361, 2521008887, 16022236204009818131831320183, 4113101149215104800030529537915953170486139623539759933135949994882770404074832568499}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube166(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VDD6FDhKCYA'
        self.title = 'Six Sequences'
        self.host = ['Tony Padilla']
        self.date = '2013-07-22'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A002210', 'https://oeis.org/A001220', 'https://oeis.org/A001462', 'http://oeis.org/A023811', 'http://oeis.org/A010727', 'http://oeis.org/A058883']
        self.wiki = ['https://en.wikipedia.org/wiki/Khinchin%27s_constant', 'https://en.wikipedia.org/wiki/Wieferich_prime', 'https://en.wikipedia.org/wiki/Golomb_sequence']
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (2.685452001065306445309714835481795693820, ), 1e-11) or result in {1093, 3511} or is_subsequence_of(context['result'][-3:], (1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18)) or is_subsequence_of(context['result'][-3:], (0, 1, 5, 27, 194, 1865, 22875, 342391, 6053444, 123456789, 2853116705, 73686780563, 2103299351334, 65751519677857, 2234152501943159, 81985529216486895, 3231407272993502984, 136146740744970718253, 6106233505124424657789, 290464265927977839335179)) or is_subsequence_of(context['result'][-3:], (7, )*3) or is_subsequence_of(context['result'][-3:], (11, 67, 2, 4769, 67)) or is_subsequence_of(context['result'][-3:], (11, 67, 2, 4769, 67))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube167(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dDl7g_2x74Q'
        self.title = 'Infinity Paradoxes'
        self.host = ['Mark Jago']
        self.date = '2013-07-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.inf])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube168(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3K-12i0jclM'
        self.title = "41 and more Ulam's Spiral"
        self.host = ['James Clewett']
        self.date = '2013-07-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 41])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube169(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=iFuR97YcSLM'
        self.title = 'Prime Spirals'
        self.host = ['James Grime']
        self.date = '2013-07-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result) or result in (3399714628553118047, 33251810980696878103150085257129508857312847751498190349983874538507313) or (is_real(result) and result > 0 and result**.5 % 1 == 0)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube170(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=j7jfHM-mMC4'
        self.title = 'Cicada 17'
        self.host = ['Steve Mould']
        self.date = '2013-06-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (17, 13)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube171(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PCu_BNNI5x4'
        self.title = 'One minus one plus one minus one'
        self.host = ['James Grime']
        self.date = '2013-06-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (0, 1, 0.5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube172(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=seUU2bZtfgM'
        self.title = 'Transcendental Numbers'
        self.host = ['Simon Pampena']
        self.date = '2013-06-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_transcendental(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube173(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Mfk_L4Nx2ZI'
        self.title = 'Zero Factorial'
        self.host = ['James Grime']
        self.date = '2013-06-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'factorial' in formula or 'gamma' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube174(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=acTrvMlpuxA'
        self.title = 'Mathematical Music'
        self.host = ['Alan Stewart']
        self.date = '2013-06-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS) or is_close(result, math.pi, 1e-5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube175(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=u17MdWjGA5I'
        self.title = 'What colour is 27?'
        self.host = ['Alex Dainis']
        self.date = '2013-05-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and (0 <= result <= 9 or result in (79, 854685254, 27))) or is_close(result, math.pi, 1e-21)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube176(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nd_Z_jZdzP4'
        self.title = 'Number Trick'
        self.host = ['James Grime']
        self.date = '2013-06-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (23483, 9999)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube177(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=D4_sNKoO-RA'
        self.title = 'Gaps between Primes (extra footage)'
        self.host = ['Ed Copeland', 'Tony Padilla']
        self.date = '2013-05-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (len(context['result']) >= 2 and is_prime(result) and is_prime(context['result'][-2]) and result-context['result'][-2] % 2 == 0) or result == 7e7 or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube178(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vkMXdShDdtY'
        self.title = 'Gaps between Primes'
        self.host = ['Ed Copeland', 'Tony Padilla']
        self.date = '2013-05-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (len(context['result']) >= 2 and is_prime(result) and is_prime(context['result'][-2]) and result-context['result'][-2] % 2 == 0) or result == 7e7 or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube179(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5JOAoiX1LHA'
        self.title = 'Googol Song'
        self.host = ['Helen Arney', 'Matt Parker']
        self.date = '2013-05-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1e100, 3e41)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube180(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=gaVMrqzb91w'
        self.title = 'Why 381,654,729 is awesome'
        self.host = ['James Grime']
        self.date = '2013-05-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (381654729, 10123457689, 362880, 3265920) or (is_int(result) and len(str(abs(int(result)))) == 9 and all(str(i) in str(result) for i in range(1, 10))) or (is_int(result) and len(str(abs(int(result)))) == 10 and all(str(i) in str(result) for i in range(0, 10)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube181(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Fmb3TCvlETk'
        self.title = 'Base Number Jokes Explained'
        self.host = ['Matt Parker']
        self.date = '2013-05-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'different bases'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (10, 2, 3, 15, 25)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube182(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=JJQWtGm3eIs'
        self.title = 'Math Jokes Explained'
        self.host = ['Matt Parker']
        self.date = '2013-05-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'cross multiplication'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (len(context['result']) > 1 and not any(is_error(r) or is_complex(r) for r in context['result'][-2:]) and context['result'][-2] != 0 and result // context['result'][-2] > 10) or result in {2, 789, 6, 7, 0, 8} or re.search(r'[^*]\*[^*]', formula)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube183(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=XvDC-0aNw2k'
        self.title = 'Numberphile in Nepal'
        self.host = ['Brady Haran']
        self.date = '2013-05-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 108, 261, 8848)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube184(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wo19Y4tw0l8'
        self.title = 'Illegal Numbers'
        self.host = ['James Grime']
        self.date = '2013-05-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (ord(c) for c in 'NUMBERPHILE') or result == 94699040255592155765623877])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube185(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ctC33JAV4FI'
        self.title = 'Infinite Primes'
        self.host = ['James Grime']
        self.date = '2013-04-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.inf or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube186(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SxP30euw3-0'
        self.title = 'Random Numbers'
        self.host = ['James Clewett']
        self.date = '2013-04-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'randomness'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result) or '%' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube187(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=noDSyLzVz2g'
        self.title = 'Random Numbers (the next bit)'
        self.host = ['James Clewett']
        self.date = '2013-04-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "normal randomness -- what's the stdev in the distribution?"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result) or result == 216])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube188(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=u7Z9UnWOJNY'
        self.title = "Zeno's Paradox"
        self.host = ['James Grime']
        self.date = '2013-04-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.inf or (is_real(result) and -1 < result < 1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube189(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=e4sF_Z5oJek'
        self.title = 'Fibonacci Tartan and Bagpipes'
        self.host = ['Brady Haran']
        self.date = '2013-04-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in FIBONACCI_NUMBERS[1:12]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube190(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Waw11zhaKSk'
        self.title = 'Safe Cracking with Feynman'
        self.host = ['Roger Bowley']
        self.date = '2013-03-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (len(context['result']) >= 3 and context['result'][-3] in ([25, 0, 25], [50, 25, 50])) or result in (8000, 162, 20) or is_close(result, (math.pi, math.e), 1e-8)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube191(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CMP9a2J4Bqw'
        self.title = 'Squaring the Circle'
        self.host = ['James Grime']
        self.date = '2013-03-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi, 1e-9) or is_transcendental(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube192(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=GyN-qpVfOWA'
        self.title = 'Statistics on Match Day'
        self.host = ['Matt Furniss', 'Sam Green']
        self.date = '2013-03-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1800, 900, 2, 3, 0, 5, 62}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube193(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WM1FFhaWj9w'
        self.title = 'Problems with French Numbers'
        self.host = ['Paul Smith']
        self.date = '2013-03-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {70, 80, 90} or any('60+'+str(i) in formula for i in (10, 19)) or '4*20' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube194(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=QzrRkhU248A'
        self.title = '19 out of 20'
        self.host = ['Paul Smith']
        self.date = '2013-03-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {20, 19, 18, 16, 14, 12, 10, 10/20, 12/20, 14/20, 16/20, 18/20, 19/20} or any('60+'+str(i) in formula for i in (10, 19)) or '4*20' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube195(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bFNjA9LOPsg'
        self.title = 'How Pi was nearly changed to 3.2'
        self.host = ['James Grime']
        self.date = '2013-03-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi, 1e-1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube196(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=x4kyFKyCMv0'
        self.title = "Pi with Pies (director's slice)"
        self.host = ['Matt Parker']
        self.date = '2013-03-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi, 0.0033) or is_close(result, (264+2/3, 84+1/3))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube197(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZNiRzZ66YN0'
        self.title = 'Calculating Pi with Real Pies'
        self.host = ['Matt Parker']
        self.date = '2013-03-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi, 0.0033) or is_close(result, (264+2/3, 84+1/3))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube198(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=iW_LkYiuTKE'
        self.title = 'The problem in Good Will Hunting'
        self.host = ['James Grime']
        self.date = '2013-03-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 10])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube199(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dNy23tJMTzQ'
        self.title = 'Synesthesia'
        self.host = ['Alex Dainis']
        self.date = '2013-02-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (0 <= result <= 10 or result == 20)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube200(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FpyrF_Ci2TQ'
        self.title = 'Pi and the size of the Universe'
        self.host = ['James Grime']
        self.date = '2013-02-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 39 or is_close(result, math.pi, 1e-38) or is_close(result, (8.8e26, 2.5e-11, 2.5e-12))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube201(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8IOaoK2MMoI'
        self.title = 'Meet James Grime'
        self.host = ['James Grime']
        self.date = '2013-02-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "base 12 -- that's where the 12 came from"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (155, math.inf, 284, 220, 1, 12) or is_close(result, 2*math.pi) or (is_int(result) and result % 2 == 0)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube202(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aOJOfh2_4PE'
        self.title = 'Zequals and Estimation'
        self.host = ['Rob Eastaway']
        self.date = '2013-02-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0 and result < math.inf])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube203(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=YJuHC7xXsGA'
        self.title = 'Anatomy of a Goal'
        self.host = ['Sam Green']
        self.date = '2013-02-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {318304, 6433, 4, 115, 54, 12237, 118, 366, 10318, 9, 62.3, 20, 5.6, 47.57, 76, 118, 136, 4611, 17, 17878, 16, 1954371119, 19.7, 47.2, 13.1, 59, 4, 154, 287890550, 1196, 16, 17676, 40997, 40998, 16, 1, 104, 108, 23}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube204(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=a9P9Ej1b31s'
        self.title = 'Quick chat with Brady'
        self.host = ['Brady Haran']
        self.date = '2013-02-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {14, 16, 11, 8, 2.5, 0}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube205(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=QSEKzFGpCQs'
        self.title = 'New Largest Known Prime Number'
        self.host = ['Tony Padilla']
        self.date = '2013-02-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (57885161, 17425170, 5, 1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube206(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wCyC-K_PnRY'
        self.title = 'Dragon Curve'
        self.host = ['Rob Eastaway']
        self.date = '2013-02-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 45 or is_close(result, 2**0.5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube207(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-rwqnVsGFTU'
        self.title = 'The Most Favourite Number'
        self.host = ['Brady Haran']
        self.date = '2013-02-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6041, 5286, 7, 3, 42, 8, 13, GRAHAMS_NUMBER, 16, 4617, 266, GOLDEN_RATIO, math.e, 2*math.pi, 42, 73, 420, 1337, 9001}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube208(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=QJQ691PTKsA'
        self.title = 'End of Time (Unix)'
        self.host = ['James Clewett']
        self.date = '2013-01-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 2147483647])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube209(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VbtNy54ya9A'
        self.title = "Brady's Videos and Benford's Law"
        self.host = ['Brady Haran']
        self.date = '2013-01-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "compare Benford's Curve to curve based on context['result'] (once there are enough of them) -- are they statistically the same?"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube210(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=XXjlR2OK1kM'
        self.title = "Number 1 and Benford's Law"
        self.host = ['Steve Mould']
        self.date = '2013-01-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube211(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=G2_Q9FoD-oQ'
        self.title = '158,962,555,217,826,360,000 (Enigma Machine)'
        self.host = ['James Grime']
        self.date = '2013-01-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {60, 17576, 150738274937250, 158962555217826360000}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube212(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mlqAvhjxAjo'
        self.title = '4937775'
        self.host = ['Ed Copeland']
        self.date = '2012-12-22'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A006753'
        self.wiki = 'https://en.wikipedia.org/wiki/Smith_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and sum([result // 10**i % 10 for i in range(math.ceil(math.log(result, 10)))]) == sum(sum([f // 10**i % 10 for i in range(math.ceil(math.log(f, 10)))]) for f in factors(result, FACTORS_PRIME))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube213(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6_j2X6fgkaA'
        self.title = 'Calculator Unboxing #8 (Printing Digits)'
        self.host = ['Matt Parker']
        self.date = '2016-08-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_error(result) and result.msg == 'divide by zero') or result in {0.99999999999, 496, 58008, 12}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube214(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=uak-wvXJAvE'
        self.title = 'Kids get their money'
        self.host = ['Brady Haran', "Danny (Brady's Neighbor)", "Emily (Brady's Neighbor)"]
        self.date = '2012-12-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4, 8, 550, 890, 10, 13}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube215(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=U6xJfP7-HCc'
        self.title = 'Base 12'
        self.host = ['James Grime']
        self.date = '2012-12-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'base 12'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 12 or (is_real(result) and any(result % b == 0 for b in (2, 3, 4, 6, 12)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube216(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=M7kEpw1tn50'
        self.title = 'Encryption and HUGE numbers'
        self.host = ['James Grime']
        self.date = '2012-12-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2048, 65537} or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube217(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VpBmt11czaI'
        self.title = 'Advent Calendar'
        self.host = ['Brady Haran']
        self.date = '2012-11-30'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1 <= result <= 25])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube218(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8t1TC-5OLdM'
        self.title = 'Is Zero Even?'
        self.host = ['James Grime', 'Roger Bowley']
        self.date = '2012-12-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube219(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=IQofiPqhJ_s'
        self.title = '1 and Prime Numbers'
        self.host = ['James Grime']
        self.date = '2012-02-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube220(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l7lP9y7Bb5g'
        self.title = 'Beautiful Card Trick'
        self.host = ['Matt Parker']
        self.date = '2012-11-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'base'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 27])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube221(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xYAU75IS40A'
        self.title = 'Spaghetti Numbers'
        self.host = ['Brady Haran', 'Danny', 'Emily']
        self.date = '2012-11-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {881, 2e107, 107, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 32, 16, 12, 14, 25, 16, 9, 28, 18, 25}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube222(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Cn3ogzLzxuM'
        self.title = '400 and Gamebooks'
        self.host = ['James Clewett']
        self.date = '2012-11-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {214, 400, 118}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube223(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aiibxmqXV9M'
        self.title = 'Tau of Phi'
        self.host = ['Phil Moriarty']
        self.date = '2012-11-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (GOLDEN_RATIO, 2*math.pi))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube224(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=uuMwz47LV_w'
        self.title = 'Keith Numbers'
        self.host = ['Ed Copeland']
        self.date = '2012-11-13'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A007629'
        self.wiki = 'http://en.wikipedia.org/wiki/Keith_number'
        self.note = "could write algorithm to determine is Keith number; there are also other numbers but can't find good list of them"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {14, 19, 28, 47, 61, 75, 197, 742, 1104, 1537, 2208, 2580, 3684, 4788, 7385, 7647, 7909, 31331, 34285, 34348, 55604, 62662, 86935, 93993, 120284, 129106, 147640, 156146, 174680, 183186, 298320, 355419, 694280, 925993, 1084051, 7913837, 11436171, 33445755, 44121607}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube225(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=83ofi_L6eAo'
        self.title = 'Tau replaces Pi'
        self.host = ['Phil Moriarty']
        self.date = '2012-11-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 2*math.pi)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube226(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=gVzu1_12FUc'
        self.title = '5 Platonic Solids'
        self.host = ['Katie Steckles', 'James Grime']
        self.date = '2012-11-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 5])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube227(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ygqIfLHGTu4'
        self.title = 'Favourite Numbers'
        self.host = ['Brady Haran', 'Derek Muller', 'Hank Green', 'Steve Spangler', 'Michael Stevens', 'Angela from YouTube EDU', 'Alex Dainis', 'Destin Sandlin', 'Mike Rugnetta', 'Caitlin from YouTube EDU', 'John Green', 'Henry Reich', 'PatrickJMT', 'CGP Grey', 'Vi Hart']
        self.date = '2012-11-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'includes j and *, which are weird numbers'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {I, 2, 17, 13, 7, 27, 21, 1024, 16, 37, 1729, 0}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube228(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3ZMnVd4ivKQ'
        self.title = 'Vampire Numbers'
        self.host = ['James Grime', 'Ed Copeland']
        self.date = '2012-10-30'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A014575'
        self.wiki = 'https://en.wikipedia.org/wiki/Vampire_number'
        self.note = "functions don't exist and vampire function not complete"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and len(str(int(result))) % 2 == 0 and result in {1260, 1395, 1435, 1530, 1827, 2187, 6880, 102510, 104260, 105210, 105264, 105750, 108135, 110758, 115672, 116725, 117067, 118440, 120600, 123354, 124483, 125248, 125433, 125460, 125500, 126027, 126846, 129640} or formula in {'2*4', '4*2'}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube229(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2dzS_LXvYA0'
        self.title = "Avogadro's Number (Mole)"
        self.host = ['Martyn Poliakoff']
        self.date = '2012-10-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 6.022140857e23, 1e14)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube230(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BRRolKTlF6Q'
        self.title = 'Problems with Zero'
        self.host = ['Matt Parker', 'James Grime']
        self.date = '2012-10-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_error(result) and result.msg == 'divide by zero') or '0**0' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube231(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fwD98HiQSJc'
        self.title = 'ViHart on Tetrahedral Dice'
        self.host = ['Vi Hart']
        self.date = '2012-10-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4, 382}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube232(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vNTSugyS038'
        self.title = 'How to order 43 Chicken McNuggets'
        self.host = ['James Grime']
        self.date = '2012-10-09'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A065003'
        self.wiki = 'https://en.wikipedia.org/wiki/Coin_problem#McNugget_numbers'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 22, 23, 25, 28, 31, 34, 37, 43}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube233(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kQZmZRE0cQY'
        self.title = "Brown's Criterion"
        self.host = ['James Grime']
        self.date = '2012-10-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and (math.log(result, 2) % 1 == 0 or result in FIBONACCI_NUMBERS)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube234(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4sUKyPYNEVA'
        self.title = 'Underwater Yahtzee'
        self.host = ['Brady Haran']
        self.date = '2012-10-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) >= 5 and all(context['result'][-1] == context['result'][i] for i in range(-5, -1))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube235(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BTyzE-NDga8'
        self.title = "Superflip and Rubik's Cube"
        self.host = ['James Grime']
        self.date = '2012-09-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 20])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube236(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yF2J39Xny4Q'
        self.title = "God's Number and Rubik's Cube"
        self.host = ['Matt Parker', 'James Grime', 'Katie Steckles']
        self.date = '2012-09-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result <= 20])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube237(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=QV9k6dRQQe4'
        self.title = "43,252,003,274,489,856,000 Rubik's Cube Combinations"
        self.host = ['Matt Parker', 'James Grime', 'Katie Steckles']
        self.date = '2012-09-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 43252003274489856000])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube238(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-Djj6pfR9KU'
        self.title = 'Brown Numbers'
        self.host = ['Ed Copeland']
        self.date = '2012-08-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'could do something fancier'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {5, 4, 11, 5, 71, 7}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube239(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=EDauz38xV9w'
        self.title = 'AMAZING Dice Rolls'
        self.host = []
        self.date = '2012-08-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) >= 5 and all(context['result'][-1] == context['result'][i] for i in range(-5, -1))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube240(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pT52hREAf18'
        self.title = 'Chinese Lucky Numbers'
        self.host = ['Xiaohui Yuan']
        self.date = '2012-08-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(d in str(result) for d in ('8', '6', '4'))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube241(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dHzUQnRjbuM'
        self.title = 'Numbery Card Trick'
        self.host = ['Matt Parker']
        self.date = '2012-08-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 12, 15, 3}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube242(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fHhnh-1Obyc'
        self.title = 'Perfect Games'
        self.host = ['Brady Haran']
        self.date = '2012-08-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {27, 300, 6, 36, 9, 501, 147, 120, 24, 1, 1575, 649739, 1/649739, 128, 130, 2044}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube243(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Dd81F6-Ar_0'
        self.title = 'One to One Million'
        self.host = ['James Grime']
        self.date = '2012-08-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 5050])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube244(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dXGhzY2p2ug'
        self.title = 'One-Roll Yahtzee Fever'
        self.host = []
        self.date = '2012-08-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) >= 5 and all(context['result'][-1] == context['result'][i] for i in range(-5, -1))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube245(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=tflf05x-WVI'
        self.title = 'Did Usain Bolt REALLY run 100m in 9.63 seconds?'
        self.host = ['Tony Padilla']
        self.date = '2012-08-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {9.63, 100, 9.62999999999999422}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube246(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=x6Ml4AEt0kk'
        self.title = 'Borromean Olympic Rings'
        self.host = ['John Hunton']
        self.date = '2012-08-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 5, 23}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube247(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=M-yAgyrzGdo'
        self.title = 'Batman Equation'
        self.host = ['James Grime']
        self.date = '2012-07-30'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_complex(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube248(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=A25pxcYstHM'
        self.title = 'Problematic Sunflower'
        self.host = ['Brady Haran']
        self.date = '2012-07-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'need efficient way to determine whether most recent two results are consecutive numbers in Fibonacci sequence'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube249(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=rKI7JINZh5Q'
        self.title = 'More One-Roll Yahtzees'
        self.host = ['Brady Haran']
        self.date = '2012-07-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) >= 5 and all(context['result'][-1] == context['result'][i] for i in range(-5, -1))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube250(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fiTwar7mFws'
        self.title = '1,296 and Yahtzee'
        self.host = ['Brady Haran']
        self.date = '2012-07-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (len(context['result']) >= 5 and all(context['result'][-1] == context['result'][i] for i in range(-5, -1))) or result in {1296, 1/1296, 64, 37, 90, 2920, 3, 627}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube251(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=p_Hqdqe84Uc'
        self.title = 'Dyscalculia'
        self.host = ['Brian Butterworth']
        self.date = '2012-07-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 4])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube252(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=EJRXWNWJOrQ'
        self.title = '37'
        self.host = ['Matt Parker']
        self.date = '2012-07-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 37])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube253(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1GCf29FPM4k'
        self.title = 'The LONGEST time'
        self.host = ['Tony Padilla']
        self.date = '2012-07-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in context['result'][:-1] and formula in context['formula'][:-1]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube254(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nBgQPSUTWVM'
        self.title = 'Golden Ratio Song'
        self.host = ['Phil Moriarty', 'Dave Brown']
        self.date = '2012-07-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, GOLDEN_RATIO)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube255(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=euAHY9hqRN4'
        self.title = '27 the Favourite Number'
        self.host = ['Katie Steckles']
        self.date = '2012-07-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {27, 6, 13598, 1, 16470, 44899}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube256(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mqK63v2Jzks'
        self.title = 'Golden Ratio - Making a Math Metal Anthem'
        self.host = ['Phil Moriarty', 'Dave Brown']
        self.date = '2012-07-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, GOLDEN_RATIO)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube257(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=elvOZm0d4H0'
        self.title = 'Infinity is bigger than you think'
        self.host = ['James Grime']
        self.date = '2012-07-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.inf])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube258(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=oIkhgagvrjI'
        self.title = 'Why do YouTube views freeze at 301?'
        self.host = ['Ted Hamilton']
        self.date = '2012-06-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 301])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube259(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MmhNk-zRJcU'
        self.title = '14 and Shakespeare the Numbers Man'
        self.host = ['Roger Bowley']
        self.date = '2012-06-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {14, 18}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube260(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8d49sEAU5Ws'
        self.title = 'The Internet is FULL'
        self.host = ['James Clewett']
        self.date = '2012-06-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4294967296, 18446744073709551616}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube261(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4mEk7d8oRho'
        self.title = '32 and Truncated Icosahedron'
        self.host = ['James Grime']
        self.date = '2012-06-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 20, 32}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube262(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yu_aqA7mw7E'
        self.title = '5, 13 and 137 are Pythagorean Primes'
        self.host = ['Laurence Eaves']
        self.date = '2012-06-07'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A002144'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149, 157, 173, 181, 193, 197, 229, 233, 241, 257, 269, 277, 281, 293, 313, 317, 337, 349, 353, 373, 389, 397, 401, 409, 421, 433, 449, 457, 461, 509, 521, 541, 557, 569, 577, 593, 601, 613, 617}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube263(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kUBIJdGsD1A'
        self.title = '10!'
        self.host = ['James Grime']
        self.date = '2012-05-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3628800, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube264(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=C-52AI_ojyQ'
        self.title = 'How big is a billion?'
        self.host = ['James Grime', 'Tony Padilla']
        self.date = '2012-05-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1e9, 1e12}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube265(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1EGDCh75SpQ'
        self.title = 'Do numbers EXIST?'
        self.host = ['Jonathan Tallant']
        self.date = '2012-06-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_number(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube266(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=R9m2jck1f90'
        self.title = '60'
        self.host = ['Thomas Woolley']
        self.date = '2012-05-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'base 60'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 60])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube267(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=RxxDD2LWAyY'
        self.title = 'What is a lucky number?'
        self.host = ['Ria Symonds']
        self.date = '2012-05-15'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A000959'
        self.wiki = 'http://en.wikipedia.org/wiki/Lucky_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99, 105, 111, 115, 127, 129, 133, 135, 141, 151, 159, 163, 169, 171, 189, 193, 195, 201, 205, 211, 219, 223, 231, 235, 237, 241, 259, 261, 267, 273, 283, 285, 289, 297, 303, 307, 319, 321, 327, 331, 339, 349, 357, 361, 367, 385, 391, 393, 399, 409, 415, 421, 427, 429, 433, 451, 463, 475, 477, 483, 487, 489, 495, 511, 517, 519, 529, 535, 537, 541, 553, 559, 577, 579, 583, 591, 601, 613, 615, 619, 621, 631, 639, 643, 645, 651, 655, 673, 679, 685, 693, 699, 717, 723, 727, 729, 735, 739, 741, 745, 769, 777, 781, 787, 801, 805, 819, 823, 831, 841, 855, 867, 873, 883, 885, 895, 897, 903, 925, 927, 931, 933, 937, 957, 961, 975, 979, 981, 991, 993, 997}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube268(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WJ12DYBuazY'
        self.title = 'Sexy Primes'
        self.host = ['James Grime']
        self.date = '2012-05-08'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A023201'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {5, 7, 11, 13, 17, 23, 31, 37, 41, 47, 53, 61, 67, 73, 83, 97, 101, 103, 107, 131, 151, 157, 167, 173, 191, 193, 223, 227, 233, 251, 257, 263, 271, 277, 307, 311, 331, 347, 353, 367, 373, 383, 433, 443, 457, 461, 503, 541, 557, 563, 571, 587, 593, 601, 607, 613, 641, 647}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube269(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CMUI6m8ZMwg'
        self.title = '8848'
        self.host = ['Brady Haran']
        self.date = '2012-05-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {8848, 200000, 1850, 200, 29000, 29002, 8840, 8850, 8844, 6268}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube270(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=UkZqFtYtqaI'
        self.title = '666'
        self.host = ['Pete Watts', 'James Grime']
        self.date = '2012-04-12'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A000217'
        self.wiki = 'https://en.wikipedia.org/wiki/Triangular_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {666, 616} or result in {0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube271(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=DRjFV_DETKQ'
        self.title = 'Sunflowers and Fibonacci'
        self.host = ['James Grime']
        self.date = '2012-04-10'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A000045'
        self.wiki = 'https://en.wikipedia.org/wiki/Fibonacci_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in FIBONACCI_NUMBERS])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube272(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=k8Rxep2Mkp8'
        self.title = 'A Hole in a Hole in a Hole'
        self.host = ['Cliff Stoll']
        self.date = '2016-09-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube273(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=XTeJ64KD5cg'
        self.title = "Graham's Number"
        self.host = ['Tony Padilla', 'Matt Parker']
        self.date = '2012-04-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Graham%27s_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {GRAHAMS_NUMBER, 7, 11, 3, 64}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube274(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=UfEiJJGv4CE'
        self.title = '3 is everywhere'
        self.host = ['James Grime']
        self.date = '2012-04-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 2 and '3' in str(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube275(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=UfEiJJGv4CE'
        self.title = '3 is everywhere'
        self.host = ['James Grime']
        self.date = '2012-04-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and '3' in str(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube276(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=U7f8j3mVMbc'
        self.title = '13,983,816 and the Lottery'
        self.host = ['James Clewett']
        self.date = '2012-03-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {14, 19, 31, 33, 34, 45, 49, 6/49, 5/48, 4/47, 3/46, 2/45, 1/44, 43/49, 42/48, 41/47, 40/46, 39/45, 38/44} or is_close(result, (720/10068347520, 4389446880/10068347520))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube277(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6R7cFk0Kihw'
        self.title = '6,000,000 and Abel Prize'
        self.host = ['James Grime']
        self.date = '2012-03-30'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 6000000 or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube278(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=QTrM-UVcgBY'
        self.title = '5 and Penrose Tiling'
        self.host = ['John Hunton']
        self.date = '2012-03-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3, 4, 5, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube279(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wPn4tgmU8ek'
        self.title = 'Sounds of Pi'
        self.host = ['Phil Moriarty']
        self.date = '2012-03-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube280(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sJVivjuMfWA'
        self.title = "Pi and Buffon's Matches"
        self.host = ['Tony Padilla']
        self.date = '2012-03-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.pi, 163/52))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube281(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=abv4Fz7oNr0'
        self.title = 'Pi and Bouncing Balls'
        self.host = ['Ed Copeland']
        self.date = '2012-03-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube282(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=abv4Fz7oNr0'
        self.title = 'Pi and Bouncing Balls'
        self.host = ['Ed Copeland']
        self.date = '2012-03-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0 and math.log(result/16, 100) % 1 < 0.001])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube283(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yJ-HwrOpIps'
        self.title = 'Pi'
        self.host = ['Alex Bellos', 'Roger Bowley']
        self.date = '2012-03-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 3+10/71 < result < 3+10/70])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube284(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=D6tINlNluuY'
        self.title = '42 and Douglas Adams'
        self.host = ['James Grime', 'Phil Moriarty', 'Gerardo Adesso']
        self.date = '2012-03-08'
        self.source = 'Numberphile'
        self.oeis = ['http://oeis.org/A002378', 'http://oeis.org/A054377', 'http://oeis.org/A005349']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 42 or result in {0, 2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272, 306, 342, 380, 420, 462, 506, 552, 600, 650, 702, 756, 812, 870, 930, 992, 1056, 1122, 1190, 1260, 1332, 1406, 1482, 1560, 1640, 1722, 1806, 1892, 1980, 2070, 2162, 2256, 2352, 2450, 2550} or result in {2, 6, 42, 1806, 47058, 2214502422, 52495396602, 8490421583559688410706771261086} or result in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81, 84, 90, 100, 102, 108, 110, 111, 112, 114, 117, 120, 126, 132, 133, 135, 140, 144, 150, 152, 153, 156, 162, 171, 180, 190, 192, 195, 198, 200, 201, 204}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube285(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=daro6K6mym8'
        self.title = '998,001 and its Mysterious Recurring Decimals'
        self.host = ['James Grime']
        self.date = '2012-03-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and is_int(result**0.5) and all('9'==d for d in str(int(result**0.5)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube286(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=DRxAVA6gYMM'
        self.title = '163 and Ramanujan Constant'
        self.host = ['Alex Clark']
        self.date = '2012-03-02'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A003173'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_complex(result) or result in {1, 2, 3, 7, 11, 19, 43, 67, 163} or result in {-1, -2, -3, -7, -11, -19, -43, -67, -163} or result in (v**0.5 for v in (-1, -2, -3, -7, -11, -19, -43, -67, -163)) or is_close(result, (math.exp(math.sqrt(v)*math.pi) for v in (1, 2, 3, 7, 11, 19, 43, 67, 163)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube287(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-O4mYiP2zPQ'
        self.title = '29 and Leap Years'
        self.host = ['Meghan Gray']
        self.date = '2012-02-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {29, 2455987, 2440423.62, 2419507.74} or (is_int(result) and result % 4 == 0 and result % 100 != 0 and result % 400 == 0)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube288(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_DpzAvb3Vk4'
        self.title = '145 and the Melancoil'
        self.host = ['Matt Parker']
        self.date = '2012-02-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {83, 38, 73, 58, 89, 145, 42, 20, 4, 16, 37}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube289(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LzjaDKVC4iY'
        self.title = '1729 and Taxi Cabs'
        self.host = ['James Grime', 'Roger Bowley']
        self.date = '2012-02-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683, 64232, 65728, 110656, 110808, 134379, 149389, 165464, 171288, 195841, 216027, 216125, 262656, 314496, 320264, 327763, 373464, 402597, 439101, 443889, 513000, 513856, 515375, 525824, 558441, 593047, 684019, 704977}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube290(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8GEebx72-qs'
        self.title = 'Googol and Googolplex'
        self.host = ['Tony Padilla', 'Ria Symonds']
        self.date = '2012-02-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, {1e100, 5e12, 1e80, 1e90, 1e183, 1e26, 1e78}, method='pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube291(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aTSYARnB-3Y'
        self.title = 'Special Magic Square'
        self.host = ['Roger Bowley']
        self.date = '2012-02-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {25, 18, 51, 82, 81, 52, 15, 28, 12, 21, 88, 55, 58, 85, 22, 11, 176}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube292(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=a2ey9a70yY0'
        self.title = '23 and Football Birthdays'
        self.host = ['James Grime']
        self.date = '2012-02-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {23, 253} or is_close(result, (0.493, 0.507), 1e-3)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube293(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kC6YObu61_w'
        self.title = '7 and Happy Numbers'
        self.host = ['Ria Symonds']
        self.date = '2012-02-10'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A007770'
        self.wiki = 'http://en.wikipedia.org/wiki/Happy_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube294(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bFfSfzjhfC8'
        self.title = '14 Super Bowl Coin Tosses'
        self.host = ['James Grime']
        self.date = '2012-02-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0.5, 14, 32766}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube295(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bFfSfzjhfC8'
        self.title = '14 Super Bowl Coin Tosses'
        self.host = ['James Grime']
        self.date = '2012-02-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube296(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=hLGDJFGAmic'
        self.title = "3/4 and Kleiber's Law"
        self.host = ['Thomas Woolley']
        self.date = '2012-01-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0.75])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube297(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5sKah3pJnHI'
        self.title = 'Root 2'
        self.host = ['Roger Bowley', 'James Grime']
        self.date = '2012-01-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 2**.5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube298(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MlyTq-xVkQE'
        self.title = '17 and Sudoku Clues'
        self.host = ['James Grime']
        self.date = '2012-01-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 81, 6.7e21, 3.3e16, 5472730538}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube299(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=hiOMtBrH8pc'
        self.title = '98 and Grafting Numbers'
        self.host = ['Matt Parker']
        self.date = '2012-01-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'interesting patterns'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {98, 99, 9998, 9999, 77, 9797, 997997, 764, 765, 5711, 5736, 76394, 2798254, 7639321, 8053139, 763932023, 76393202251, 7639320225003} or is_close(result, 3-5**.5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube300(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9xbJ3enqLnA'
        self.title = '15 and Hexadecimal'
        self.host = ['James Clewett']
        self.date = '2012-01-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'base 16'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {15, 16, 255, 0xffffffff}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube301(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mhJY74Bw8mw'
        self.title = '3435'
        self.host = ['Matt Parker']
        self.date = '2012-01-13'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A046253'
        self.wiki = 'https://en.wikipedia.org/wiki/Munchausen_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3435, 1}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube302(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4aMtJ-V26Z4'
        self.title = '153 and Narcissistic Numbers'
        self.host = ['Ria Symonds']
        self.date = '2012-01-03'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A005188'
        self.wiki = 'https://en.wikipedia.org/wiki/Narcissistic_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, 4679307774, 32164049650, 32164049651}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube303(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PLL0mo5rHhk'
        self.title = '31 and Mersenne Primes'
        self.host = ['James Grime']
        self.date = '2012-01-09'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000668'
        self.wiki = 'https://en.wikipedia.org/wiki/Mersenne_prime'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3, 7, 31, 127, 8191, 131071, 524287, 2147483647, 2305843009213693951, 618970019642690137449562111, 162259276829213363391578010288127, 170141183460469231731687303715884105727}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube304(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Oev332D0K0I'
        self.title = '15 bumfit'
        self.host = ['Roger Bowley', 'Tich Rivett']
        self.date = '2011-12-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'base 20'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {15}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube305(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fUSZBVYZdKY'
        self.title = '220 and 284 (Amicable Numbers)'
        self.host = ['James Grime']
        self.date = '2011-12-19'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A259180'
        self.wiki = 'https://en.wikipedia.org/wiki/Amicable_numbers'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) > 1 and is_int(result) and result > 0 and is_int(context['result'][-2]) and context['result'][-2] > 0 and sum(factors(result)) == context['result'][-2] and sum(factors(context['result'][-2])) == result])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube306(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kw6l_uTakRA'
        self.title = '69!'
        self.host = ['Laurence Eaves']
        self.date = '2011-12-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {69, math.factorial(69)} or is_close(result, sys.float_info.max, method='pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube307(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=d8TRcZklX_Q'
        self.title = '6147'
        self.host = ['Roger Bowley']
        self.date = '2011-12-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6147}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube308(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZfKTD5lvToE'
        self.title = '8128 and Perfect Numbers'
        self.host = ['James Grime']
        self.date = '2011-11-28'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000396'
        self.wiki = 'http://www.wikipedia.org/wiki/Perfect_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176, 191561942608236107294793378084303638130997321548169216}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube309(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mLQNvuZH3GU'
        self.title = '16'
        self.host = ['Ria Symonds', 'Matt Parker']
        self.date = '2011-11-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 16])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube310(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=umYvFdU54Po'
        self.title = '255 and Pac-Man'
        self.host = ['James Clewett']
        self.date = '2011-11-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'base 2'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 255])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube311(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sPFWfAxIiwg'
        self.title = '11.11.11'
        self.host = ['James Grime']
        self.date = '2011-11-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result < 1e11 and sum([result//(10**(10-i-1)) % 10 * (10-i) for i in range(10)]) % 11])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube312(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sPFWfAxIiwg'
        self.title = '11.11.11'
        self.host = ['James Grime']
        self.date = '2011-11-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 11])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube313(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7zGwbiCKLHs'
        self.title = 'Sun Explosion compared to the Destruction of Planet Alderaan'
        self.host = ['Matt Parker']
        self.date = '2011-06-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 2.2e3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube314(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=T6A0v3xYl7k'
        self.title = "In Defiance of Wadsworth's Constant"
        self.host = ['Matt Parker']
        self.date = '2011-10-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 0.3, 1e-3)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube315(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=RP8jepN3zMc'
        self.title = 'Matt Parker: Stand-up Maths Routine (about barcodes)'
        self.host = ['Matt Parker']
        self.date = '2011-12-06'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and 0 <= result < 1e14 and 10 - ((sum([result//(10**(13-i-1)) % 10 for i in range(0, 12, 2)]) + 3*sum([result//(10**(13-i-1)) % 10 for i in range(1, 12, 2)])) % 10) == result % 10])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube316(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nv0Onj3wXCE'
        self.title = 'The Castle and the Princess Puzzle'
        self.host = ['Matt Parker']
        self.date = '2011-11-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'solution to puzzle may be incorrect'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 4])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube317(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aPD_OkjnCqU'
        self.title = "How to Cheat and Look Like You Can Solve the Rubik's Cube"
        self.host = ['Matt Parker']
        self.date = '2012-01-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {105, 12}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube318(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Sdz0dRhsoLs'
        self.title = 'Transit of Venus - Why it comes in pairs every 100ish years'
        self.host = ['Matt Parker']
        self.date = '2012-06-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {584, 215.5, 224.70069, 365.25, 1/224.70069, 1/365.25, 1/224.70069 - 1/365.25, 1/(1/224.70069 - 1/365.25)} or is_close(result, 1/(1/224.70069 - 1/365.25))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube319(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ryFvH4Ejaxo'
        self.title = 'How to make Instant Icecream using a Fire Extinguisher'
        self.host = ['Matt Parker']
        self.date = '2013-03-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, -80, 1, 0.5} or is_close(result, 23, 1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube320(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ryFvH4Ejaxo'
        self.title = 'How to make Instant Icecream using a Fire Extinguisher'
        self.host = ['Matt Parker']
        self.date = '2013-03-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 52 or is_close(result, (1/52, 35.7, 51/52))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube321(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=G_OuIVOGDr8'
        self.title = 'The 27 Card Trick'
        self.host = ['Matt Parker']
        self.date = '2014-03-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {27, random.randrange(1, 28), 49, random.randrange(1, 50), 2, 3} or is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube322(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OpLU__bhu2w'
        self.title = 'The 10,000 Domino Computer'
        self.host = ['Matt Parker', 'Katie Steckles']
        self.date = '2014-04-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'base 2'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '+' in formula or result in {36, 2, 8, 10, 10000, 9, 3, 12} or (is_int(result) and 0 <= result <= 31) or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube323(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Ngj0a57Rlb0'
        self.title = 'Calculating pi by weighing a circle'
        self.host = ['Matt Parker']
        self.date = '2015-03-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi, 1e-2) or result in {54.2, 68.8}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube324(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qYAdXm69l8g'
        self.title = 'Calculating pi with a pendulum'
        self.host = ['Matt Parker']
        self.date = '2015-03-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.pi/4, math.pi**2/6)) or result in {31.28} or is_close(result, math.pi, 1e-2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube325(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=g7TGA-EzBHM'
        self.title = "Matt Parker's Micro-Month: MARCH 2015"
        self.host = ['Matt Parker']
        self.date = '2015-04-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1000000, 1/1000000, 2.68}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube326(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ieUvzy6rnnw'
        self.title = 'Solar Eclipse Maths and the Cosmic Coincidence of the Saros Cycle'
        self.host = ['Matt Parker']
        self.date = '2015-03-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (985, 400, 389, 29.53059, 363396, 405504, 27.55455, 30, 5.1, 27.212221, 40.7, 223, 239, 242, 18+(11+8/24)/365.2425, 3.7), method='pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube327(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kdCJunw_Jgg'
        self.title = 'NAND Cat [original]'
        self.host = ['Matt Parker']
        self.date = '2015-04-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'base 2'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0, 1, 3.58}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube328(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=zXoJlRFbktw'
        self.title = 'Sydney: The Unsuccessful Hunt for Parabolas'
        self.host = ['Matt Parker']
        self.date = '2015-06-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '^2' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube329(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=rT1sIVqonE8'
        self.title = 'Matt meets Jordan Ellenberg: 0.999999... = ?'
        self.host = ['Matt Parker', 'Jordan Ellenberg']
        self.date = '2015-06-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube330(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qJiVhfR_XVE'
        self.title = 'Matt meets Jordan Ellenberg: BONUS FOOTAGE'
        self.host = ['Matt Parker', 'Jordan Ellenberg']
        self.date = '2015-06-14'
        self.source = 'standupmaths'
        self.oeis = 'http://oeis.org/A002162'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 0, -1, 1/2, math.inf, 2, math.e} or is_close(result, math.log(2), 1e-5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube331(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pOx_daJT_8c'
        self.title = 'How to get infinitely many lottery tickets'
        self.host = ['Matt Parker']
        self.date = '2015-10-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {49, 59, math.inf} or is_close(result, (1/13983816, 1/45057474, 1/10.258, 1/40665099))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube332(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=W1OkVkq2vFM'
        self.title = 'Killing Maths Mosquitoes with Atomic Proofs: roots of two, Fermat and prime numbers'
        self.host = ['Matt Parker']
        self.date = '2015-10-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {358, 210, 26} or '2^' in formula or result in (199 + i*210 for i in range(10)) or result in (43142746595714191 + i*5283234035979900 for i in range(26))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube333(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Quwvw0vYkRA'
        self.title = 'NYC: The Linear Equation of Broadway'
        self.host = ['Matt Parker']
        self.date = '2015-11-02'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1811, 4, 12, 5, 24, 224, 95, 243, 59201, 59049, 6, 33, 7, 45, 9, 65, 10, 71, 9.975, -26.5, 0.995} or formula in {'9.975*Ans-26.5', 'Ans/10+2.7'}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube334(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lP58mP8Wchc'
        self.title = 'Matt Explains: The Lottery [featuring: Choose Function, Infinite Geometric Series]'
        self.host = ['Matt Parker']
        self.date = '2015-11-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'choose function'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {59, 6, 45057474, 40665099, 33469099} or is_close(result, (2219e-11, 0.00000002988), 1e-4, method='pct') or is_close(result, (0.09748, 0.2572, 1.3462), 1e-3)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube335(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=YfIQ7ktFM1g'
        self.title = "Sam's Home-made Disco Calculator"
        self.host = ['Matt Parker', 'Sam Headleand']
        self.date = '2015-11-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_error(result) and result.msg == 'divide by zero') or formula in {'2-3', 'Ans/0', '-1/Ans', '0^0', '25×37'} or result in {0.7734, 2, 30, 3000, 925, 954, 5678} or is_close(result, (2**0.5, math.pi, 2*math.pi))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube336(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=E5-pgBnGyzw'
        self.title = 'The Share the Power Puzzle'
        self.host = ['Matt Parker']
        self.date = '2015-11-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'potential for more'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {14, 70, 60, 620, 7200}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube337(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=prh72BLNjIk'
        self.title = 'The Fairest Sharing Sequence Ever'
        self.host = ['Matt Parker']
        self.date = '2015-11-27'
        self.source = 'standupmaths'
        self.oeis = ['http://oeis.org/A036577', 'http://oeis.org/A010060']
        self.wiki = 'https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence'
        self.note = 'base 2'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (2, 1, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 0, 2, 0, 1, 2, 0, 2, 1, 0, 1, 2, 1, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 0, 1, 2, 1, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 0, 2, 0, 1, 2, 0, 2, 1, 0, 1, 2, 1, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 0, 1, 2, 1, 0, 2, 0, 1, 2, 1, 0)) or is_subsequence_of(context['result'][-3:], (0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube338(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=oJ7uOj2LRso'
        self.title = 'There are SIX Platonic Solids'
        self.host = ['Matt Parker']
        self.date = '2015-11-30'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {5, 12}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube339(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-EhaFDv-OvU'
        self.title = 'Doing Nothing on Platform Zero'
        self.host = ['Matt Parker']
        self.date = '2015-12-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube340(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Pcgvv6T_bD8'
        self.title = "Matt Explains: Binomial Coefficients [featuring: choose function, pascal's triangle]"
        self.host = ['Matt Parker']
        self.date = '2015-12-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'choose function'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) >= 5 and context['result'][-5:] == [1, 4, 6, 4, 1]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube341(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BIiEsIDenTk'
        self.title = 'How to Make a Paper Snowflake'
        self.host = ['Matt Parker']
        self.date = '2015-12-22'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 6])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube342(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=UBX2QQHlQ_I'
        self.title = 'Stand-up comedy routine about Spreadsheets'
        self.host = ['Matt Parker']
        self.date = '2016-01-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result <= 255])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube343(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=07PBcmGozDA'
        self.title = "James Grime's Maths Puzzle: The self descriptive number"
        self.host = ['Matt Parker']
        self.date = '2016-01-06'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 6210001000])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube344(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SOgn6J12NWE'
        self.title = 'The A4 Paper Puzzle'
        self.host = ['Matt Parker']
        self.date = '2016-01-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'base 64 hash of perimeter from SHA-256'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (0.7083, 0.001389), 1e-4, 'pct') or is_close(result, (2**.5, 0.02)) or result in {1, 234477, 42, 5004, 4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube345(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Me9fCKNvBBE'
        self.title = 'Australian Bank Notes are the Best in the World'
        self.host = ['Matt Parker']
        self.date = '2016-01-18'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 5, 20, 10, 100, 50} or 'ln' in formula or is_close(result, (0.99742, 0.99486, 0.99747, 0.99812))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube346(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=q5ozBnrd5Zc'
        self.title = 'New World-Record Largest Prime Ever Found!'
        self.host = ['Matt Parker', 'Curtis Cooper']
        self.date = '2016-01-19'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and (str(result).startswith('300376') or str(result).endswith('86436351'))) or result in {22338618, 2567, 74207281} or is_close(result, 800, 0.05, 'pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube347(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9KABcmczPdg'
        self.title = 'The Unbeatable Game from the 60s: Dr NIM'
        self.host = ['Matt Parker']
        self.date = '2016-01-26'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 12 or '%4' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube348(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aNpGxZ_1KXU'
        self.title = 'Mind-boggling Card Trick (you can try at home)'
        self.host = ['Matt Parker']
        self.date = '2016-02-02'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 52])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube349(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=V3uNDe_i_1Y'
        self.title = 'Mind-boggling Card Trick: REVEALED'
        self.host = ['Matt Parker']
        self.date = '2016-02-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {52, 26}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube350(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qMP7_IQpSN0'
        self.title = 'Spinning Egg Trick (feat. Tippe Top)'
        self.host = ['Matt Parker']
        self.date = '2016-02-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1890, 68, 69}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube351(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=hoh4TmPzu1w'
        self.title = 'There is only One True Parabola'
        self.host = ['Matt Parker']
        self.date = '2016-03-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'parabola'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube352(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qkt_wmRKYNQ'
        self.title = 'Leap Years: we can do better'
        self.host = ['Matt Parker']
        self.date = '2016-02-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'base 2'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (365+(5+(48+45.138/60)/60)/24, 365.2421897), 1e-8) or result in {46, 265.25, 4, 128, 1752, 3216, 625000, 53.5e12, 1.7, 1.7e-3, 52e-3, 2048} or is_close(result, 3372000, method='pct') or is_close(result, 365, 1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube353(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qkt_wmRKYNQ'
        self.title = 'Leap Years: we can do better'
        self.host = ['Matt Parker']
        self.date = '2016-02-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 4 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube354(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qkt_wmRKYNQ'
        self.title = 'Leap Years: we can do better'
        self.host = ['Matt Parker']
        self.date = '2016-02-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 4 == 0 and result % 100 != 0 and result % 400 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube355(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qkt_wmRKYNQ'
        self.title = 'Leap Years: we can do better'
        self.host = ['Matt Parker']
        self.date = '2016-02-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 4 == 0 and result % 100 != 0 and result % 400 == 0 and (result % 10000) % 2800 != 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube356(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qkt_wmRKYNQ'
        self.title = 'Leap Years: we can do better'
        self.host = ['Matt Parker']
        self.date = '2016-02-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 4 == 0 and result % 128 != 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube357(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qkt_wmRKYNQ'
        self.title = 'Leap Years: we can do better'
        self.host = ['Matt Parker']
        self.date = '2016-02-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 4 == 0 and result % 128 != 0 and result % 625024 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube358(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=owVwjr6pTqc'
        self.title = 'Paraboloids and The Building which Set Things on Fire'
        self.host = ['Matt Parker']
        self.date = '2016-02-16'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'parabola, tan'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1/4])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube359(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=G7zT9MljJ3Y'
        self.title = 'Fair Dice (Part 1)'
        self.host = ['Persi Diaconis']
        self.date = '2016-09-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4, 6, 8, 20, 12, 30, math.inf, 24}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube360(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7hJ4Azr--s8'
        self.title = 'Prisoners in Hats Puzzle: two variations'
        self.host = ['Matt Parker']
        self.date = '2016-03-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1000, 1001, 998, 997} or is_close(result, (0.5, 2/3))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube361(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HrRMnzANHHs'
        self.title = 'Calculating π by hand'
        self.host = ['Matt Parker']
        self.date = '2016-03-13'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (3.04183997892940221112, 0.760459994732350))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube362(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aHU-L3BLd_w'
        self.title = '10 coin flips in a row! (for 10^5 subscribers)'
        self.host = ['Matt Parker']
        self.date = '2016-03-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1e5, 0.5**10}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube363(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8pj8_zjelDo'
        self.title = 'The Fractal Menger Sponge and Pi'
        self.host = ['Matt Parker']
        self.date = '2016-04-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {20, 0, math.inf} or is_close(result, (math.pi, 4/3*math.pi))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube364(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xHh0ui5mi_E'
        self.title = 'The Three Indistinguishable Dice Puzzle'
        self.host = ['Matt Parker']
        self.date = '2016-04-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1 <= result <= 18 or '%' in formula or result == 216])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube365(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_o0cIpLQApk'
        self.title = "Ramanujan, 1729 and Fermat's Last Theorem"
        self.host = ['Matt Parker']
        self.date = '2016-04-28'
        self.source = 'standupmaths'
        self.oeis = 'http://oeis.org/A050791'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1729, 12, 635318657, 65601, 67402, 83802}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube366(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_o0cIpLQApk'
        self.title = "Ramanujan, 1729 and Fermat's Last Theorem"
        self.host = ['Matt Parker']
        self.date = '2016-04-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: [1, 2, 3] == context['result'][-3:]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube367(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_o0cIpLQApk'
        self.title = "Ramanujan, 1729 and Fermat's Last Theorem"
        self.host = ['Matt Parker']
        self.date = '2016-04-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: [1, 4, 9] == context['result'][-3:]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube368(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_o0cIpLQApk'
        self.title = "Ramanujan, 1729 and Fermat's Last Theorem"
        self.host = ['Matt Parker']
        self.date = '2016-04-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: [1, 1, 2] == context['result'][-3:]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube369(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ggH8cKcPOHI'
        self.title = 'Quick Mathematical Card Trick'
        self.host = ['Matt Parker']
        self.date = '2016-05-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1 <= result <= 52])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube370(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=hBBftD7gq7Y'
        self.title = 'SOLUTION: Three Indistinguishable Dice Puzzle'
        self.host = ['Matt Parker']
        self.date = '2016-05-16'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and 1 <= result <= 18) or '%' in formula or result in {120, 90, 6, 216} or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube371(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=hBBftD7gq7Y'
        self.title = 'SOLUTION: Three Indistinguishable Dice Puzzle'
        self.host = ['Matt Parker']
        self.date = '2016-05-16'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'TODO: complete the msg function ...'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False and all(is_int(context['result'][-i]) and 1 <= context['result'][-i] <= 6 for i in (1, 2, 3))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube372(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xVBOlbjiHGI'
        self.title = 'A new Rhombic Dodecahedron from Croatia!'
        self.host = ['Matt Parker']
        self.date = '2016-05-26'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 20, 30} or is_close(result, ((2*(1+1/5**.5))**.5, (2*(1-1/5**.5))**.5, 2**.5, GOLDEN_RATIO))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube373(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yfR1Jkl5R8A'
        self.title = 'The Best Square Square in New York'
        self.host = ['Matt Parker']
        self.date = '2016-06-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {14, 62.5, 67, 67.5} or is_close(result, (40.7605364,-73.9881165, 40.7475166,-73.9902623, 40.7417129,-73.9866145, 40.7362828,-73.9934595, 40.7334896,-73.9846672, 40.730503,-73.9959379, 40.7274296,-73.9929123, 40.7268115,-73.9832778, 40.7226714,-73.9878349, 40.7152103,-74.001972, 40.7147475,-73.9910052, 40.7140132,-73.9990492, 40.712846,-73.9964231, 40.7047231,-74.0104991), 1e-7) or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube374(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-9FWBaWah28'
        self.title = 'SOLUTION: 10 coin flips in a row! (for 10^5 subscribers)'
        self.host = ['Matt Parker']
        self.date = '2016-06-19'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {939, 10016, 1024, 512, 10, 42, 500, 314, 666, 2046, 1000, 256, 420, 2048, 200, 100, 250, 300, 100000, 1023, 50, 1, 1337, 1234, 150, 2036, 600, 188, 183, 160, 85, 78, 72, 68, 66, 64, 63, 63, 50, 49, 47, 43, 40, 40, 38, 37, 36, 34, 33, 32, 32, 31, 914, 510, 411, 8950} or is_close(result, (2045.97, 426239.3, 2036.3, 939.5), 1e-2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube375(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=x0gRcRd_rHs'
        self.title = 'The maths of spherical video (aka "360 camera")'
        self.host = ['Matt Parker', 'Henry Segerman']
        self.date = '2016-06-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {190, 1920, 1080, 960, 360, 180} or is_complex(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube376(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Gh8h8MJFFdI'
        self.title = 'Puzzle: Is 36 the only triangle-square number?'
        self.host = ['Matt Parker']
        self.date = '2016-07-13'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = "formula in {'x^2', 'x*(x+1)/2'}"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {36, 6, 8}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube377(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=cwWBpjeyRS0'
        self.title = 'Geometry of Footballs and the Cube-shaped Ball'
        self.host = ['Matt Parker']
        self.date = '2016-07-21'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 20, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube378(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5Yy_unGaD-w'
        self.title = 'How many different Youtube videos are possible?'
        self.host = ['Matt Parker']
        self.date = '2016-07-27'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1920, 1080, 256, 65536, 50, 128, 110863792} or is_close(result, (2.6e157826, 1e15, 4e17, 1e82), 1e-2, 'pct') or is_close(result, (1924.3, 29368779.7, 13.9, 73.4), 1e-2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube379(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=s94Gojs3Ags'
        self.title = 'How to mathematically calculate a fall through the Earth'
        self.host = ['Matt Parker']
        self.date = '2016-08-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (6.67e-11, 5.972e24), 1e-2, 'pct') or is_close(result, math.pi) or is_close(result, (2530.5, 42+10.5/60, 7909.5, 17693, 28474), 1e-1) or result == 5514])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube380(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CCuaWqhVvIc'
        self.title = 'Milk first or last? The correct method for hot tea. (GONE MATHEMATICAL)'
        self.host = ['Matt Parker']
        self.date = '2016-08-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '^4' in formula or is_close(result, (0, 2.5), 0.1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube381(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=H18pyUN4U1M'
        self.title = 'Polygons of New York'
        self.host = ['Matt Parker']
        self.date = '2016-08-26'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 4, 30, 20, 8} or is_close(result, GOLDEN_RATIO)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube382(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=55gJgCoDld4'
        self.title = 'Matt & Hugh: The Euler Disk Which Spins Forever'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2016-08-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {math.inf, 5.1, 0.81, 28.2, 0.16, 0.056}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube383(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LYKn0yUTIU4'
        self.title = 'Four has Four Letters'
        self.host = ['Matt Parker']
        self.date = '2016-09-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4, 3, 5, 6, 18, 13} or (len(context['result']) >= 6 and [23, 11, 6, 3, 5, 4] == context['result'][-6:])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube384(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AvO4s3bW-qI'
        self.title = "Manchester Mega Pixel: world's largest analogue digital image"
        self.host = ['Matt Parker', 'Katie Steckles']
        self.date = '2016-09-22'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {120, 72, 8640}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube385(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3GJUM6pCpew'
        self.title = 'Why is TV 29.97 frames per second?'
        self.host = ['Matt Parker']
        self.date = '2016-10-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {29.97, math.inf, 525, 262.5, 60, 30, 6, 4.5, 6e6, 4.5e6, 0.25, 0.25e6, 25, 625, 6, 6e6, 384, 625, 240} or is_close(result, 4.5e6/15750, 0.2857) or is_close(result, 15734.25, 15.75)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube386(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4k1jegU4Wb4'
        self.title = 'The mystery of 0.577'
        self.host = ['Tony Padilla']
        self.date = '2016-10-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.inf or (is_real(result) and result > 0 and is_int(math.log2(result)) and math.log2(result) < 0) or is_close(result, math.exp(100), 1e-1, 'pct') or is_close(result, 0.57721566490153286060)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube387(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=uCsD3ZGzMgE'
        self.title = 'The Josephus Problem'
        self.host = ['Daniel Erman']
        self.date = '2016-10-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube388(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-scs_yF59YE'
        self.title = 'The bridge which is measured in smoots'
        self.host = ['Matt Parker']
        self.date = '2016-10-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {364.4, 5+7/12, 5*12+7, 1962}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube389(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=W18FDEA1jRQ'
        self.title = 'The Seven Bridges of Königsberg'
        self.host = ['Cliff Stoll']
        self.date = '2016-11-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {7, 5}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube390(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VEsFoinLHrk'
        self.title = "New Rubik's Cube World Record! 4.74 seconds"
        self.host = ['Matt Parker', 'Mats Valk']
        self.date = '2016-11-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 4.74])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube391(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=cZ1W1vbuYuQ'
        self.title = 'MathsJam 2016: Letterwise Magic Squares'
        self.host = ['Matt Parker']
        self.date = '2016-11-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1729, 133625910214620404953, 0x4753011fdb5d2ba37ebb6be33f5376d7529a3f67, 0xe5572030fdb915f2defaff2e121158b5fb16116c8439419310dfd120ca745222, 135, 162, 165, 45} or (len(context['result']) >= 2 and any(is_subsequence_of(context['result'][:-3], seq) for seq in ((41, 72, 21, 24, 45, 66, 69, 18, 48), (8, 10, 9, 10, 9, 8, 9, 8, 10), (15, 72, 48, 78, 45, 12, 41, 18, 75), (18, 69, 48, 75, 45, 15, 42, 21, 72), (47, 61, 57, 67, 54, 41, 51, 47, 64), (48, 62, 58, 68, 55, 42, 52, 48, 65), (8, 19, 18, 25, 15, 5, 12, 11, 22), (5, 22, 18, 28, 15, 2, 12, 8, 25), (4, 9, 8, 11, 7, 3, 6, 5, 10))))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube392(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=49KvZrioFB0'
        self.title = 'Mondrian Puzzle'
        self.host = ['Gordon Hamilton']
        self.date = '2016-11-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) >= 2 and is_subsequence_of(context['result'][-3:], (2, 4, 4, 5, 5, 6, 6, 8, 6, 7, 8, 9, 9, 9, 8, 10, 9, 9, 9, 9, 9, 9))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube393(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5kC5k5QBqcc'
        self.title = 'The Problems with Secret Santa'
        self.host = ['Hannah Fry']
        self.date = '2016-11-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube394(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xu-RSUGBgpA'
        self.title = 'Too Many Triangles'
        self.host = ['Henry Segerman']
        self.date = '2016-11-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {60, 3, 4, 5, 6, 7, 8, 60*3, 60*4, 60*5, 60*6, 60*7}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube395(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=QvvkJT8myeI'
        self.title = 'The Shortest Ever Papers'
        self.host = ['Tony Padilla']
        self.date = '2016-12-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4, 5}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube396(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ubQXz5RBBtU'
        self.title = 'The Mathematics of Winning Monopoly'
        self.host = ['Matt Parker', 'Hannah Fry']
        self.date = '2016-12-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6.3, 39, 100, 1000000, 0, 2.1, 0.021, 3.2, 0.032, 1.2, 0.012, 83, 1500, 2.854, 2.109, 1.919, 2.261, 2.404, 2.757, 2.317, 1.017, 2.308, 2.278, 6.325, 2.719, 2.61, 2.395, 2.477, 2.804, 2.8, 2.62, 2.94, 3.096, 2.868, 2.839, 1.212, 2.731, 3.197, 2.897, 2.719, 2.689, 2.821, 2.601, 0, 2.675, 2.616, 1.116, 2.494, 2.553, 2.239, 2.085, 2.086, 2.552, 0.02854, 0.02109, 0.01919, 0.02261, 0.02404, 0.02757, 0.02317, 0.01017, 0.02308, 0.02278, 0.06325, 0.02719, 0.0261, 0.02395, 0.02477, 0.02804, 0.028, 0.0262, 0.0294, 0.03096, 0.02868, 0.02839, 0.01212, 0.02731, 0.03197, 0.02897, 0.02719, 0.02689, 0.02821, 0.02601, 0, 0.02675, 0.02616, 0.01116, 0.02494, 0.02553, 0.02239, 0.02085, 0.02086, 0.02552} or (is_real(result) and (4 < result < 4.125 or 0.04 < result < 0.04125)) or result in range(2, 13)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube397(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8dHMpnfFdtc'
        self.title = 'Super Bottle'
        self.host = ['Carlo Séquin']
        self.date = '2016-12-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 3}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube398(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AuA2EAgAegE'
        self.title = "e (Euler's Number)"
        self.host = ['James Grime']
        self.date = '2016-12-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'formulas'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.e)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube399(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pF8goco4ix0'
        self.title = 'The Numbers in Dice Stacking and Balancing'
        self.host = ['Matt Parker']
        self.date = '2016-12-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (any(0 < len(context['result'])*(m+1)-m <= result <= len(context['result'])*(m+1)-1 for m in (6, 12, 20, 120)) or result in {6, 12, 20, 120, 7, 13, 21, 605, 242, 363, 3}) or result == 60.5])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube400(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8hsZm1BD_j8'
        self.title = 'The Curious Incident of the Maths in the Stage-show: Part 1'
        self.host = ['Matt Parker', 'Bunny Christie', 'Alan Bain']
        self.date = '2016-12-21'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result) or result == 1./25])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube401(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=shQnyNlgmkc'
        self.title = 'The Curious Incident of the Maths in the Stage-show: Part 2'
        self.host = ['Matt Parker', 'Adrian Sutton']
        self.date = '2016-12-21'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube402(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xgBGibfLD-U'
        self.title = 'Incredible Formula'
        self.host = ['James Grime']
        self.date = '2016-12-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: formula in ('(1+9^(-4^(6×7)))^(3^(2^85))', '2^(5^.4)-.6-(.3^9/7)^(.8^.1)') or result == 18457734525360901453873570 or is_close(result, math.e)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube403(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=z6jMU-AwX34'
        self.title = '17 Number Facts about 2017 in 2:17'
        self.host = ['Matt Parker']
        self.date = '2016-12-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'bases 8, 31, 32'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {17, 2011, 2017, 2027, 10, 2008, 2026, 11, 2009, 2019, 2010, 7000, 2018, 1997, 2029, 504, 1993, 2081, 252, 1889, 2081, 126, 63, 1039, 2011, 2111, 1777, 2069, 1993, 2137, 1009, 1879, 2029, 33, 1327, 22, 1973, 1892, 2146, 232, 2015, 2018, 349, 13358, 8} or formula in {'9^2+44^2', '44^2+3^4'}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube404(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=TV7sbaffuNo'
        self.title = 'How to make an edge-coloured origami dodecahedron'
        self.host = ['Matt Parker']
        self.date = '2016-12-26'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 30, 3, 4, 5, 20, 24} or (5, 3) in {tuple(context['result'][-2:]), tuple(context['result'][:-3:-1])}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube405(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1MtEUErz7Gg'
        self.title = 'Sandpiles'
        self.host = ['Luis David Garcia-Puente']
        self.date = '2017-01-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'multi-dimensional values, additive identity'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0, 262144} or is_close(result, 100000, 0.10, 'pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube406(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ETrYE4MdoLQ'
        self.title = 'The Feigenbaum Constant (4.669)'
        self.host = ['Ben Sparks']
        self.date = '2017-01-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'formula of the form lambda*Ans*(1-Ans), for lambda in (0, 4)'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 4.669201609102990671853203821578)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube407(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yadjZTBDSR4'
        self.title = 'Measuring the Berlin TV Tower with a ruler'
        self.host = ['Matt Parker']
        self.date = '2017-02-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2.8, 160, 1./160} or is_close(result, 368, 80)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube408(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Noo4lN-vSvw'
        self.title = 'The Four 4s'
        self.host = ['Alex Bellos']
        self.date = '2017-02-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube409(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PQDvEJFdY1U'
        self.title = '383 is cool'
        self.host = ['Matt Parker']
        self.date = '2017-02-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'prime, palindrome, sum of first three 3-digit palindromic primes, smallest number that is the sum of a prime and its reverse, Woodall prime (n* 2^n -1)'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {383}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube410(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PQDvEJFdY1U'
        self.title = '383 is cool'
        self.host = ['Matt Parker']
        self.date = '2017-02-15'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A050918'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {7, 23, 383, 32212254719, 2833419889721787128217599, 195845982777569926302400511, 4776913109852041418248056622882488319, 1307960347852357218937346147315859062783, 225251798594466661409915431774713195745814267044878909733007331390393510002687}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube411(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=X3HDnrehyDM'
        self.title = 'Frog Jumping'
        self.host = ['Gordon Hamilton']
        self.date = '2017-02-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and float(result) > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube412(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xhj5er1k6GQ'
        self.title = 'The Illumination Problem'
        self.host = ['Howard Masur']
        self.date = '2017-02-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube413(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AGX0cLbHaog'
        self.title = 'Problems with Periodic Orbits'
        self.host = ['Howard Masur']
        self.date = '2017-03-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube414(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Ku8BOBwD4hc'
        self.title = 'Stable Rollers'
        self.host = ['Tadashi Tokieda']
        self.date = '2017-03-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube415(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FkHjG759ABY'
        self.title = 'Recreating Asteroids with Lasers'
        self.host = ['Matt Parker', 'Seb Lee-Delisle']
        self.date = '2017-03-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube416(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0iMtlus-afo'
        self.title = "Pascal's Triangle"
        self.host = ['Casandra Monroe']
        self.date = '2017-03-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Pascal%27s_triangle'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and result % 11 == 0) or (result in {3, 5, 17, 257, 65537}) or (result in {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169})])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube417(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=RZBhSi_PwHU'
        self.title = 'Generating π from 1,000 random numbers'
        self.host = ['Matt Parker']
        self.date = '2017-03-13'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {500, 31, 27, 60, 10, 18, 23, 1, 38, 111, 114, 34, 98, 120, 15, 93, 12, 21, 113, 41, 169, 100, 24, 61, 45, 63, 322, 178, 1000} or (is_number(result) and is_close(result, 6 / math.pi**2, 0.028, 'pct')) or is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube418(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MXJ-zpJeY3E'
        self.title = "The World's Best Mathematician (*)"
        self.host = ['Terry Tao']
        self.date = '2017-03-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube419(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NgbK43jB4rQ'
        self.title = 'The Four Color Map Theorem'
        self.host = ['James Grime']
        self.date = '2017-03-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (0 < result < 5 or result in {125, 1936, 1482})])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube420(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=EYkBctqyKic'
        self.title = 'The Brick Double-Domino Effect Explained'
        self.host = ['Matt Parker']
        self.date = '2017-03-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube421(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=rXfKWIZQIo4'
        self.title = 'The Moving Sofa Problem'
        self.host = ['Dan Romik']
        self.date = '2017-03-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.pi/2, math.pi/2 + 2/math.pi, 2.2195, 16.6, 0.289653820817320941, 0.124712637587267758, 0.5, -0.167049816550309655, -0.458812270687887068, 0.875287362412732241, 1.202938908156911389, -0.498273610464875672, 0.875287362412732241, 1.645)) or result in {18, 0}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube422(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=rXvaCy8PMdE'
        self.title = 'The Brick Balancing Challenge'
        self.host = ['Matt Parker']
        self.date = '2017-03-27'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 5, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube423(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LqKpkdRRLZw'
        self.title = 'Collatz Conjecture in Color'
        self.host = ['Alex Bellos', 'Tiffany Arment']
        self.date = '2017-03-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1 <= result <= 10000])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube424(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4dUK1JqTSgU'
        self.title = 'Reflected Cats'
        self.host = ['Tadashi Tokieda']
        self.date = '2017-04-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube425(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-ruC5A9EzzE'
        self.title = 'The 10,958 Problem'
        self.host = ['Matt Parker']
        self.date = '2017-04-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (100 <= result <= 999 or result < 11111)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube426(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pasyRUj7UwM'
        self.title = 'A 10,958 Solution'
        self.host = ['Matt Parker']
        self.date = '2017-04-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and is_close(result, 10958, 0.4)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube427(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kbKtFN71Lfs'
        self.title = 'Chaos Game'
        self.host = ['Ben Sparks']
        self.date = '2017-04-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'randomness'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == random.randint(1, 6) or is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube428(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ur-iLy4z3QE'
        self.title = "Apéry's constant (calculated with Twitter)"
        self.host = ['Tony Padilla']
        self.date = '2017-05-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 1.202056903159594, 1.2083-1.202056903159594)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube429(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3inLMXcetUA'
        self.title = 'Calculating the optimal sphere packing density with oranges'
        self.host = ['Matt Parker', 'Steve Mould']
        self.date = '2017-05-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'tetrahedral number, triangle numbers, square number'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, math.pi/(18**.5)}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube430(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WN58941sgtI'
        self.title = 'Speed Unboxing - Calculator Unboxing #9'
        self.host = ['Matt Parker']
        self.date = '2017-05-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'includes matching formulas'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: formula in {'2^.5', '2^0.5', '2^(1/2)', '2*^*tan(', '2×^×tan(', '5×6'} or result in {2041, 31 + 8/60, 31*60+8} or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube431(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NzfSombRHIM'
        self.title = 'UK Rubik’s Cube Championship 2016 PART I'
        self.host = ['Matt Parker', 'Callum Hales-Jepp', 'Elizabeth at the UK Rubik’s Cube Championship 2016']
        self.date = '2017-05-22'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and result < 30) or result in {13, 20, 24, 41, 36.837, 17.368, 1.58, 2.74, 29.16, 125} or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube432(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MxiTG96QOxw'
        self.title = 'Goldbach Conjecture'
        self.host = ['David Eisenbud']
        self.date = '2017-05-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 2 and result % 2 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube433(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MxiTG96QOxw'
        self.title = 'Goldbach Conjecture'
        self.host = ['David Eisenbud']
        self.date = '2017-05-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 5 and result % 2 == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube434(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ndEVnYhCMzo'
        self.title = 'UK Rubik’s Cube Championship 2016 PART II'
        self.host = ['Matt Parker', 'Katie Steckles', 'Jessie', 'Alexander Lau']
        self.date = '2017-05-26'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result) or result in {80.424, 1.3404, 76.726, 1.2787666666666666, 66.31, 66.31/60, 64.626, 1.0771, 63.21, 1.0535, 65.84, 1.097333333333333, 2*60+27, 2+27/60, 62.13, 62.13/60, 147, 148, 64.47, 64.47/60, 64.62, 64.62/60, 7.071}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube435(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PEMIxDjSRTQ'
        self.title = '210 is VERY Goldbachy'
        self.host = ['Carl Pomerance']
        self.date = '2017-05-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6, 8, 10, 12, 14, 16, 18, 24, 30, 36, 42, 48, 60, 90, 210}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube436(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=O4ndIDcDSGc'
        self.title = "Gödel's Incompleteness Theorem"
        self.host = ['Marcus du Sautoy']
        self.date = '2017-05-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube437(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mccoBBf0VDM'
        self.title = "Gödel's Incompleteness (extra footage 1)"
        self.host = ['Marcus du Sautoy']
        self.date = '2017-06-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube438(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OWCAlJ1vsqc'
        self.title = 'How fast is a Fidget Spinner?'
        self.host = ['Matt Parker']
        self.date = '2017-06-02'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {62.5, 1571, 15.7, 56.5, 35.1}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube439(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NoRjwZomUK0'
        self.title = 'Squared Squares'
        self.host = ['James Grime']
        self.date = '2017-06-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {21, 112, 50, 35, 27, 15, 17, 11, 8, 19, 29, 25, 9, 16, 18, 24, 33, 37, 42, 6, 2, 4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube440(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=I0peG_kRE-4'
        self.title = 'A Nice Square'
        self.host = ['James Grime']
        self.date = '2017-06-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {39, 42, 31, 3, 11, 9, 20, 36, 33, 14, 5, 19, 24, 2320, 1885, 1040, 429, 234, 182, 52, 130, 195, 91, 13, 117, 104, 325, 221, 299, 957, 725, 638, 143, 78, 65, 312, 286, 39, 247, 705, 565, 615, 87, 551, 493, 319, 522, 435, 174, 145, 140, 375, 50, 696, 667, 665, 575, 270, 203, 232, 406, 116, 35, 340, 305, 290, 29, 261}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube441(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3IMAUm2WY70'
        self.title = '13532385396179'
        self.host = ['Tony Padilla']
        self.date = '2017-06-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 13532385396179])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube442(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=RhuaPhahHbU'
        self.title = '4D MONKEY DUST'
        self.host = ['Henry Segerman']
        self.date = '2017-06-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'dimensions'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube443(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ezdeBrPnzyc'
        self.title = 'A Quick Cake Conundrum'
        self.host = ['Cliff Stoll']
        self.date = '2017-06-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube444(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=m6rfpQXzXu0'
        self.title = 'Math vs Physics'
        self.host = ['Robbert Dijkgraaf']
        self.date = '2017-06-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube445(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=uhuqp7CVmxw'
        self.title = "Matt meets Feliks Zemdegs: Rubik's Cube World Champion"
        self.host = ['Matt Parker', 'Feliks Zemdegs']
        self.date = '2017-07-06'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4.73, 0.01, 7.03, 5.55, 5.25, 4.9, 43.2, 60*2+18, 2*60+7, 3.52, 150, 8.36}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube446(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lpj0E0a0mlU'
        self.title = 'How many particles in the Universe?'
        self.host = ['Tony Padilla']
        self.date = '2017-07-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {8.64e-30, 0.0485, 4.38e28, 1.67e-24, 3.28e80, 2.25e51, 1.11, 7.5e9, 8604}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube447(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nP1elMR5qjc'
        self.title = 'Rolling Shutter Explained on the Cheap'
        self.host = ['Matt Parker']
        self.date = '2017-07-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2e3, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube448(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BH1GMGDYndo'
        self.title = 'Large Gaps between Primes'
        self.host = ['James Maynard']
        self.date = '2017-07-19'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A002386'
        self.wiki = None
        self.note = "there's an equation for estimating the length of a gap between primes for large values, but it depends on a variable that's underspecified to use here"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 3, 7, 23, 89, 113, 523, 887, 1129, 1327, 9551, 15683, 19609, 31397, 155921, 360653, 370261, 492113, 1349533, 1357201, 2010733, 4652353, 17051707, 20831323, 47326693, 122164747, 189695659, 191912783, 387096133, 436273009, 1294268491}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube449(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=r4dUCsse6_A'
        self.title = "Speed Rubik's Cubing for drunk people"
        self.host = ['Matt Parker', 'Feliks Zemdegs']
        self.date = '2017-07-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube450(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LOVzytir7bM'
        self.title = 'Brilliant Geometry: a physical 3D zoetrope of a 4D cube'
        self.host = ['Matt Parker', 'Henry Segerman']
        self.date = '2017-07-19'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube451(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=co5sOgZ3XcM'
        self.title = 'The Kolakoski Sequence'
        self.host = ['Alex Bellos']
        self.date = '2017-07-24'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000002'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube452(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MTfviv_aZYI'
        self.title = 'Exploring Hyperbolic Space with VR (and crochet)'
        self.host = ['Matt Parker', 'Henry Segerman', 'Sabetta Matsumoto']
        self.date = '2017-07-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'hyperbolic space'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6, 7, 8}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube453(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pbXg5EI5t4c'
        self.title = 'Derangements'
        self.host = ['James Grime']
        self.date = '2017-07-31'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000002'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube454(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aCq04N9it8U'
        self.title = 'Aaron Numbers'
        self.host = ['Carl Pomerance']
        self.date = '2017-08-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {714, 715} or (len(context['result']) >= 2 and context['result'][-2:] in ((5, 6), (14, 15), (714, 715), (5, 6), (8, 9), (15, 16), (77, 78), (125, 126), (714, 715), (948, 949), (1330, 1331), (1520, 1521), (1862, 1863), (2491, 2492), (3248, 3249), (4185, 4186), (4191, 4192), (5405, 5406), (5560, 5561), (5959, 5960), (6867, 6868), (8280, 8281), (8463, 8464), (10647, 10648), (12351, 12352), (14587, 14588), (16932, 16933), (17080, 17081), (18490, 18491)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube455(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HcqdqsQq-6M'
        self.title = 'When do clock hands overlap?'
        self.host = ['Cliff Stoll']
        self.date = '2017-08-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (12/11, 12/11*3600))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube456(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=G_uybVKBacI'
        self.title = 'Braids in Higher Dimensions'
        self.host = ['Zsuzsanna Dancso']
        self.date = '2017-08-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 2, 3, 4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube457(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=eHN7OJuVgXA'
        self.title = 'The Raising of Chicago: the windy city'
        self.host = ['Matt Parker']
        self.date = '2017-08-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1856, 1858, 1897} or (is_real(result) and 4 <= result <= 14) or result in {750, 200, 3400} or is_close(result, (6+2/12, 4+8/12))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube458(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9tlHQOKMHGA'
        self.title = 'What does i^i = ?'
        self.host = ['Matt Parker']
        self.date = '2017-09-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'could use better formula parsing'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(val in formula for val in ('e', 'i', 'π', 'sin', 'cos')) or formula == 'i^i' or is_close(result, math.exp(-math.pi/2))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube459(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fQQ8IiTWHhg'
        self.title = 'The Trinity Hall Prime'
        self.host = ['Tadashi Tokieda']
        self.date = '2017-09-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "that's a prime number"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1350, 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888111111111111111111111111888888111111111111111111111111888888111111811111111118111111888888111118811111111118811111888888111188811111111118881111888888111188811111111118881111888888111888811111111118888111888888111888881111111188888111888888111888888111111888888111888888111888888888888888888111888888111888888888888888888111888888111888888888888888888111888888811188888888888888881118888188811188888888888888881118881188881118888888888888811188881118888111888888888888111888811111888811118888888811118888111111188881111111111111188881111111118888111111111111888811111111111888811111111118888111111111111188881111111188881111111111111118888811118888811111111111111111888881188888111111111111111111118888888811111111111111111111111888888111111111111111111111111118811111111111111111111111111111111111111111111062100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube460(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=EeuLDnOupCI'
        self.title = 'The Neverending Story (and Droste Effect)'
        self.host = ['Cliff Stoll']
        self.date = '2017-09-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 108])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube461(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mceaM2_zQd8'
        self.title = 'Strange Spheres in Higher Dimensions'
        self.host = ['Matt Parker']
        self.date = '2017-09-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'dimensions'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, [i**.5 - 1 for i in range(2, 13)]) or result == 4])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube462(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FlndIiQa20o'
        self.title = 'Casting Out Nines'
        self.host = ['James Grime']
        self.date = '2017-09-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'TODO: casting out nines'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 9])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube463(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pdMZjssrAlk'
        self.title = 'The Coriolis Effect Test: two hemispheres, one sink'
        self.host = ['Matt Parker']
        self.date = '2017-09-19'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube464(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dFvzUNMU1Lo'
        self.title = 'Postcards from backstage: Katie and Semi-Eulerian Graphs'
        self.host = ['Matt Parker', 'Katie Steckles']
        self.date = '2017-09-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: all(is_int(r) and r > 0 for r in context['result']) and sum(1 for r in context['result'] if r % 2 == 1) in (0, 2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube465(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kaMKInkV7Vs'
        self.title = 'Equally sharing a cake between three people'
        self.host = ['Hannah Fry']
        self.date = '2017-09-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result == 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube466(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=b23i3NhFLDc'
        self.title = 'Postcards from backstage: Hugh and the Wall of Death Units'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2017-09-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result >= 6.56])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube467(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7dwgusHjA0Y'
        self.title = 'Juggling by Numbers'
        self.host = ['Colin Wright']
        self.date = '2017-09-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube468(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AB-FA75Tm1I'
        self.title = 'Postcards from backstage: Rob and the Anti-Monty-Hall Problem'
        self.host = ['Matt Parker', 'Rob Eastaway']
        self.date = '2017-10-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (1/3, 3/5))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube469(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=btPqKAGyajM'
        self.title = 'All UK football road signs are wrong! Join the petition for geometric change!'
        self.host = ['Matt Parker']
        self.date = '2017-10-09'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0, 2, 5, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube470(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9yUZTTLpDtk'
        self.title = 'Secrets to measuring a piece of paper'
        self.host = ['Cliff Stoll']
        self.date = '2017-10-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube471(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=XXcWQWO-uHg'
        self.title = 'Matt & Hugh: Euler Disk III, The Correctioning'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2017-10-18'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube472(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3P6DWAwwViU'
        self.title = 'The Enormous TREE(3)'
        self.host = ['Tony Padilla']
        self.date = '2017-10-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "very big number (bigger than Graham's number)"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: [1, 3] == context['result'][-2:]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube473(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=m3drS_8BpU0'
        self.title = 'Pancake Numbers'
        self.host = ['Katie Steckles']
        self.date = '2017-10-27'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A058986'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube474(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4LQvjSf6SSw'
        self.title = 'Fibonacci Numbers hidden in the Mandelbrot Set'
        self.host = ['Holly Krieger']
        self.date = '2017-10-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in FIBONACCI_NUMBERS or isinstance(result, complex)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube475(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=oKY-s6IvZkE'
        self.title = 'Matt & Hugh: the mystery of two balls in a can'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2017-11-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 3} or is_close(result, 2.0/3, 1e-5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube476(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4kWuxfVbIaU'
        self.title = 'The Ideal Auction'
        self.host = ['Preston McAfee']
        self.date = '2017-11-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube477(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fcVjitaM3LY'
        self.title = '78557 and Proth Primes'
        self.host = ['James Grime']
        self.date = '2017-11-13'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A080076'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {78557, 10223,  21181, 22699, 24737, 55459, 67607} or (is_real(result) and result > 1e300 and 10223*2**31172165+1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube478(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=R9c-_neaxeU'
        self.title = 'MENACE: the pile of matchboxes which can learn'
        self.host = ['Matt Parker', 'Matthew Scroggs', 'Katie Steckles']
        self.date = '2017-11-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {304, 10**43, 10**170}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube479(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=L4xOtyUgtZ8'
        self.title = 'Back to the Fax Machine'
        self.host = ['Matt Parker']
        self.date = '2017-11-21'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2015, 1414042559}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube480(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=un-pTKfC1dQ'
        self.title = 'An unexpected way to inflate a balloon'
        self.host = ['Tadashi Tokieda']
        self.date = '2017-11-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'randomness'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube481(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2BIx2x-Q2fE'
        self.title = 'An astonishing old calculator'
        self.host = ['Cliff Stoll']
        self.date = '2017-11-30'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result) or is_rational(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube482(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=A8Tiba3h9Fw'
        self.title = "Don Bradman's Duck"
        self.host = ['Brady Haran']
        self.date = '2017-12-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1000, 0, 52, 1908, 50, 100, 6996, 70, 99.94}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube483(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZoA0u66wcSs'
        self.title = 'Strictly Come Dancing is Strictly Unfair'
        self.host = ['Matt Parker', 'Jen Rogers']
        self.date = '2017-12-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and 1 <= result <= 12) or (len(context['result']) > 1 and result == context['result'][-2])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube484(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZcB6FfAxKlY'
        self.title = 'Stats of CERN: How many Higgs per second?'
        self.host = ['Matt Parker']
        self.date = '2017-12-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {120e9, 2500, int(120e9)*2500, 11245, 7, 12, 25e-9, 40e6, 25, 1e9, 1, 10, 2.5, 6.499e9, }])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube485(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=YCXmUi56rao'
        self.title = 'Ham Sandwich Problem'
        self.host = ['Hannah Fry']
        self.date = '2017-12-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Ham_sandwich_theorem'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0.5 or (is_int(result) and result > 0)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube486(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZCVAGb1ee8A'
        self.title = 'River Crossings (and Alcuin Numbers)'
        self.host = ['Annie Raymond']
        self.date = '2018-01-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'computes the vertex cover of a graph'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube487(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=G1m7goLCJDY'
        self.title = 'The Square-Sum Problem'
        self.host = ['Matt Parker']
        self.date = '2018-01-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'interesting math/visual here'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0 and math.sqrt(result) % 1 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube488(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=i3D7XYQExt0'
        self.title = 'Calculating a Car Crash'
        self.host = ['Ben Sparks']
        self.date = '2018-01-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube489(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5SfXqTENV_Q'
        self.title = 'Cannons and Sparrows'
        self.host = ['Günter Ziegler']
        self.date = '2018-01-22'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A024619'
        self.wiki = None
        self.note = 'could do pattern matching on the formula'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and len(set(factors(result, FACTORS_PRIME))) == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube490(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l7E-pBWuSIA'
        self.title = 'Numbers with Meaning'
        self.host = ['Sarah Wiseman']
        self.date = '2015-06-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'technically, the test is whether the number is one *you* are familiar with'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube491(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=p-xa-3V5KO8'
        self.title = 'Tree Gaps and Orchard Problems'
        self.host = ['Ben Sparks']
        self.date = '2018-01-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.inf, lambda formula, result, context: len(context['result']) > 1 and is_int(result) and is_int(context['result'][-2]) and Fraction(result, context['result'][-2]).numerator == result, lambda formula, result, context: is_close(result, 6/math.pi**2) or is_close(result, GOLDEN_RATIO)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube492(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wJGE4aEWc28'
        self.title = 'Superpermutations'
        self.host = ['James Grime']
        self.date = '2018-01-29'
        self.source = 'Numberphile'
        self.oeis = ['http://oeis.org/A180632']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 121, 123121321, 123412314231243121342132413214321, 123451234152341253412354123145231425314235142315423124531243512431524312543121345213425134215342135421324513241532413524132541321453214352143251432154321, 12345612345162345126345123645132645136245136425136452136451234651234156234152634152364152346152341652341256341253641253461253416253412653412356412354612354162354126354123654132654312645316243516243156243165243162543162453164253146253142653142563142536142531645231465231456231452631452361452316453216453126435126431526431256432156423154623154263154236154231654231564213564215362415362145362154362153462135462134562134652134625134621536421563421653421635421634521634251634215643251643256143256413256431265432165432615342613542613452613425613426513426153246513246531246351246315246312546321546325146325416325461325463124563214563241563245163245613245631246532146532416532461532641532614532615432651436251436521435621435261435216435214635214365124361524361254361245361243561243651423561423516423514623514263514236514326541362541365241356241352641352461352416352413654213654123}, lambda formula, result, context: result in {1, 3, 9, 33, 153, 872}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube493(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wJGE4aEWc28'
        self.title = 'Superpermutations'
        self.host = ['James Grime']
        self.date = '2018-01-29'
        self.source = 'Numberphile'
        self.oeis = ['http://oeis.org/A180632']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube494(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Us-__MukH9I'
        self.title = "Catalan's Conjecture"
        self.host = ['Holly Krieger']
        self.date = '2018-02-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 8, 9}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube495(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FtNWzlfEQgY'
        self.title = 'Conway Checkers'
        self.host = ['Zvezdelina Stankova']
        self.date = '2018-02-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 4, 8, 20}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube496(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AvFNCNOyZeE'
        self.title = 'Round Peg in a Square Hole'
        self.host = ['Tadashi Tokieda']
        self.date = '2018-03-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.sqrt(2))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube497(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AZRD5UkAm2Y'
        self.title = 'Number Sticks'
        self.host = ['Katie Steckles']
        self.date = '2018-03-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 18 and str(int(result))[0] == '1' and str(int(result))[-1] == '8' and all(c == '9' for c in str(int(result))[1:-1])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube498(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mthPiiCS24A'
        self.title = 'Dealing Cards with Cryptography (with Ron Rivest)'
        self.host = ['Ron Rivest']
        self.date = '2018-03-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'cryptography, Q^(j*k) mod prime'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result) and len(str(result)) >= 100])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube499(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3Bv-QMaYlmo'
        self.title = 'Combinatorics and Higher Dimensions'
        self.host = ['Federico Ardila']
        self.date = '2018-04-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'combinatorics'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube500(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BDEo5XpZcXo'
        self.title = 'Neon Knots and Borromean Beer Rings'
        self.host = ['Cliff Stoll']
        self.date = '2018-04-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube501(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bPZFQ6i759g'
        self.title = 'Is the "hot hand" real?'
        self.host = ['Lisa Goldberg']
        self.date = '2018-04-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 0.5, 0.1) or result == 31/44 or context['result'][-44:] == [int(i) for i in '11011110010111111001110111101110111101010101']])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube502(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aKPkQCys86c'
        self.title = 'The Math (and money) of Soccer Stickers'
        self.host = ['Federico Ardila']
        self.date = '2018-04-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'contains a formula'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {682, 1, 0.2, 136.4, 109.12, 4844, 968.8, 775.04, 1775, 355, 284, }])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube503(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wZ1E_CM7MqA'
        self.title = 'The Pentomino Puzzle (and Tetris)'
        self.host = ['Alex Bellos']
        self.date = '2018-05-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {5, 12, 64}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube504(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_pP_C7HEy3g'
        self.title = 'The Coin Hexagon'
        self.host = ['Alex Bellos']
        self.date = '2018-05-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube505(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sj8Sg8qnjOg'
        self.title = 'The Golden Ratio (why it is so irrational)'
        self.host = ['Ben Sparks']
        self.date = '2018-05-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (GOLDEN_RATIO, 1-GOLDEN_RATIO))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube506(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7lRgeTmxnlg'
        self.title = 'The Silver Ratio'
        self.host = ['Tony Padilla']
        self.date = '2018-05-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.sqrt(2)-1), lambda formula, result, context: is_prime(len(context['result'])) and is_prime(result), lambda formula, result, context: result in {0, 1, 169}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube507(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7lRgeTmxnlg'
        self.title = 'The Silver Ratio'
        self.host = ['Tony Padilla']
        self.date = '2018-05-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'limit computation in last test'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.sqrt(2)-1, (3 + math.sqrt(13))/2)), lambda formula, result, context: formula == '(Ans + (Ans^2 + 4)^0.5) / 2', lambda formula, result, context: is_close(result, [(n + math.sqrt(n**2 + 4))/2 for n in range(4, 1000)])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube508(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1gBwexpG0IY'
        self.title = 'The Problem with 7825'
        self.host = ['James Grime']
        self.date = '2018-05-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 7825])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube509(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4445Mbw8pYg'
        self.title = 'g-conjecture'
        self.host = ['June Huh']
        self.date = '2018-05-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'palindromic numbers'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0, 1, 2}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube510(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=hHG8io5qIU8'
        self.title = "Weber's Law"
        self.host = ['Hannah Fry']
        self.date = '2018-05-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'log' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube511(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FGC5TdIiT9U'
        self.title = 'The Slightly Spooky Recamán Sequence'
        self.host = ['Alex Bellos']
        self.date = '2018-06-14'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A005132'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62, 42, 63, 41, 18, 42, 17, 43, 16, 44, 15, 45, 14, 46, 79, 113, 78, 114, 77, 39, 78, 38, 79, 37, 80, 36, 81, 35, 82, 34, 83, 33, 84, 32, 85, 31, 86, 30, 87, 29, 88, 28, 89, 27, 90, 26, 91, 157, 224, 156, 225, 155))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube512(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6H6EP-AmMFM'
        self.title = 'Floating Balls and Lift'
        self.host = ['Tadashi Tokieda']
        self.date = '2018-06-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube513(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=DhPtIf-hpuU'
        self.title = 'The Six Triperfect Numbers'
        self.host = ['James Grime']
        self.date = '2018-06-29'
        self.source = 'Numberphile'
        self.oeis = ['http://oeis.org/A005820', 'http://oeis.org/A027687', 'http://oeis.org/A046060']
        self.wiki = 'https://en.wikipedia.org/wiki/Multiply_perfect_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {120, 672, 523776, 459818240, 1476304896, 51001180160}, lambda formula, result, context: result in {30240, 32760, 2178540, 23569920, 45532800, 142990848, 1379454720, 43861478400, 66433720320, 153003540480, 403031236608, 704575228896, 181742883469056, 6088728021160320, 14942123276641920, 20158185857531904, 275502900594021408}, lambda formula, result, context: result in {14182439040, 31998395520, 518666803200, 13661860101120, 30823866178560, 740344994887680, 796928461056000, 212517062615531520, 69357059049509038080, 87934476737668055040, 170206605192656148480, 1161492388333469337600, 1245087725796543283200, 1802582780370364661760, 1940351499647188992000, 4010059765937523916800, 27099073228001299660800, 143573364313605309726720, 352338107624535891640320, 34384125938411324962897920, 686498980761986918441287680, 2827987212986831882236723200, 72746008559331545135067955200, 115131961034430181728489308160, 2360137508360958913826987704320, 13361233986454282110797768294400, 32789312424503984621373515366400, 80538025176927765566622699356160, 217722929396007151091289843302400, 534305825433598205172314957414400, 6204968071598247960303205991055360, 45018882179216278209289221235015680, 13188979363639752997731839211623940096, 636279286816242760423054379770183680000, 900809435698475541919724282581258076160, 5027991804154655285871782854518594600960, 17955160408011298190208066009641779200000, 69401922567934198070320735661287916175360, 5157152737616023231698245840143799191339008, 54530444405217553992377326508106948362108928, 133821156044600922812153118065015159487725568, 1966044603041307019027644125759103098242990080, 42274041475824304453686528060845522019324411248640, 4989680372093758991515359988337845750507257510078971904, 48949643430560436794021629524876790263031553747866371344635527168, 713287896776577122497355829377640852485760737912531339949234978816, 23361923592618741050590062043477131121314459866398752235742822400000, 38686788011121056578700900574076814908809553749239322473792016482304, 57713546223799971103662580404885081100965146124863318716687633612800, 44828737039702888991401809596138010582841359879253837507147347271876608, 68688966922031309945174465761834751373920047004215278394826366933532672, 34493877198688394697394823968609123706029600512135632542151228195491282944, 26858749569550544873070080560343416018763475799423745716289183150310797869056, 54765047586062826077147104232519533773657166644091409455081090503841475985408, 97718179472691973067025524016904045403285849149449049247269303180639070060544, 1058432493851272505433162341756539259435410113004034309326827312980982497280000, 13487790701729822904972967765042898578513187190976458260434978753935365910822912, 88551677944411242892294975443276201965497448498065529379599857155248300425740288, 6549096139588623356377131453027611949713035117549335458597551434741879668736000000, 413868115397556203624257790605260143631946430317607991092410053640572227750461440000, 1606376105545205480958192524197465863877796712608687336011572840200748052216415256576, 6506613515483667018449676450491160367057969293776979604120864113095261465533634052096, 34625463861934857866504118671022510711069778103433886737026425811008293190601250177024, 2560826592715906873441737348908544954304137097588021202695037291512948842433609728000000, 18863735795135429357926598339727034593434784361635488470523830097438618848151197459265574980259151872}, lambda formula, result, context: result in {154345556085770649600, 9186050031556349952000, 680489641226538823680000, 6205958672455589512937472000, 13297004660164711617331200000, 15229814702070563916152832000, 34111227434420791224041472000, 36669339708545656151565926400, 41254809330254618094796800000, 52693888533626064627302400000, 59023729003862626557345792000}, lambda formula, result, context: result in {141310897947438348259849402738485523264343544818565120000, 15502381086169113100250590183664788846018448946703031358518722560000, 318169247391962748189900043049059135703522232534529605673943040000000, 409782874235824708837450606126936069129304803154874054366103339008000}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube514(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=u_xQ_C5RUfo'
        self.title = 'How to make a Klein Bottle from an old pair of jeans'
        self.host = ['Cliff Stoll']
        self.date = '2018-07-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube515(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ffvojZONF_A'
        self.title = 'The Cross Ratio'
        self.host = ['Federico Ardila']
        self.date = '2018-07-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 1.251, 3) or result in {5.5, 16.5, 11, 1.3, 3.2, 4.5, 7.3, 16.5, 16.63}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube516(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=d7dg7gVDWyg'
        self.title = '21-card trick'
        self.host = ['Anastasia Chavez']
        self.date = '2018-07-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 21 or 'mod' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube517(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2vnqSwWAn34'
        self.title = 'Earthquakes, Circles and Spheres'
        self.host = ['Tadashi Tokieda']
        self.date = '2018-07-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3 or is_close(result, (3, 6), 0.1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube518(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lubGnk0UZt0'
        self.title = 'Balls and Cones'
        self.host = ['Tadashi Tokieda']
        self.date = '2018-07-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube519(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=azL5ehbw_24'
        self.title = '357686312646216567629137'
        self.host = ['James Grime']
        self.date = '2018-07-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and any(result == 357686312646216567629137 % (10**(len(str(int(357686312646216567629137)))-i)) for i in range(len(str(int(357686312646216567629137))))), lambda formula, result, context: is_int(result) and result > 0 and any(result == 73939133 // (10**(len(str(int(73939133)))-i)) for i in range(len(str(int(73939133))))), lambda formula, result, context: is_int(result) and result > 0 and (any(result == 739397 // (10**(len(str(int(739397)))-i)) for i in range(len(str(int(739397))))) or any(result == 739397 % (10**(len(str(int(739397)))-i)) for i in range(len(str(int(739397)))))), lambda formula, result, context: result in {415673, 45673, 4567, 467, 67, 7}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube520(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l9dXo5f3zDc'
        self.title = 'Chinese Remainder Theorem and Cards'
        self.host = ['Tadashi Tokieda']
        self.date = '2018-08-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '%' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube521(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=n7GYYerlQWs'
        self.title = '5-Sided Square'
        self.host = ['Cliff Stoll']
        self.date = '2018-08-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 5*90])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube522(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=G2Blr0LycOI'
        self.title = 'Antipodal Points'
        self.host = ['Simon Pampena']
        self.date = '2018-08-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube523(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=U33dsEcKgeQ'
        self.title = 'The Dollar Game'
        self.host = ['Holly Krieger']
        self.date = '2018-08-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'genus of graph'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube524(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FUD8h9JpEVQ'
        self.title = 'Does Hollywood ruin books?'
        self.host = ['Hannah Fry']
        self.date = '2018-08-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube525(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=cjx23aMeBkQ'
        self.title = 'Golden Ratio BURN (Internet Beef)'
        self.host = ['Matt Parker']
        self.date = '2018-09-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, GOLDEN_RATIO), lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS), lambda formula, result, context: is_subsequence_of(context['result'][-3:], LUCAS_NUMBERS)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube526(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=c4pgWd8V8HU'
        self.title = 'Floating Bodies'
        self.host = ['Elisabeth Werner']
        self.date = '2018-09-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube527(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OKhacWQ2fCs'
        self.title = 'Every Number is the Sum of Three Palindromes'
        self.host = ['James Grime']
        self.date = '2018-09-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'Great message opportunities'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube528(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CROeIGfr3gs'
        self.title = 'The Best Way to Pack Spheres'
        self.host = ['James Grime']
        self.date = '2018-09-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi/(3*math.sqrt(2)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube529(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LZ7X_YOfJqY'
        self.title = 'Kissing Numbers'
        self.host = ['James Grime']
        self.date = '2018-10-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 24, 240, 196500}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube530(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=T46FTuHnbvY'
        self.title = 'Spheres and Code Words'
        self.host = ['James Grime']
        self.date = '2018-10-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {math.pi/(2*math.sqrt(3)), math.pi/(3*math.sqrt(2)), math.pi**4/384, math.pi**12/math.factorial(12)} or is_close(result, (math.pi**2/16, math.pi**2/(15*math.sqrt(2)), math.pi**3/(48*math.sqrt(3)), math.pi**3/105))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube531(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=zk_Q9y_LNzg'
        self.title = 'The Most Evil Number'
        self.host = ['Tony Padilla']
        self.date = '2018-10-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {16661, 1000000000000066600000000000001}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube532(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=cZkGeR9CWbk'
        self.title = 'Primes on the Moon (Lunar Arithmetic)'
        self.host = ['Neil Sloane']
        self.date = '2018-11-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'very interesting message possibilities'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: True])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube533(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=D3tdW9l1690'
        self.title = 'A Strange Map Projection (Euler Spiral)'
        self.host = ['Hannah Fry']
        self.date = '2018-11-13'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'maps'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube534(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZMkIiFs35HQ'
        self.title = 'Squaring Primes'
        self.host = ['Matt Parker']
        self.date = '2018-11-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 3 and (result - 1) % 24 == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube535(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OeGSQggDkxI'
        self.title = 'What Number Comes Next?'
        self.host = ['Neil Sloane']
        self.date = '2018-11-26'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A249572', 'https://oeis.org/A087409', 'http://oeis.org/A002904', 'https://oeis.org/A006933', 'https://oeis.org/A006567']
        self.wiki = None
        self.note = 'sequences'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(result in s for s in ({1, 4, 8, 48, 88, 488, 888, 4888, 8888, 48888, 88888, 488888, 888888, 4888888, 8888888, 48888888, 88888888, 488888888, 888888888, 4888888888, 8888888888, 48888888888, 88888888888, 488888888888, 888888888888, 4888888888888, 8888888888888, 48888888888888}, {61, 21, 82, 43, 3, 64, 24, 85, 46, 6, 67, 27, 88, 49, 9, 61, 2, 10, 81, 14, 12, 1, 26, 13, 21, 38, 14, 41, 50, 15, 61, 62, 16, 81, 74, 18, 1, 86, 19, 21, 98, 20, 42, 10, 21, 62, 22, 22, 82, 34, 24, 2, 46, 25, 22, 58, 26, 42, 70, 27, 62, 82, 28, 82, 94, 30, 3, 6, 31, 23, 18, 32, 43}, {0, 0, 0, 0, 4, 9, 5, 1, 1, 0, 55, 55, 1, 0, 1, 9, 5, 1, 1, 0, 0, 0, 0, 0, 4, 9, 5, 1, 1, 1, 1, 1, 1, 1}, {2, 4, 6, 30, 32, 34, 36, 40, 42, 44, 46, 50, 52, 54, 56, 60, 62, 64, 66, 2000, 2002, 2004, 2006, 2030, 2032, 2034, 2036, 2040, 2042, 2044, 2046, 2050, 2052, 2054, 2056, 2060, 2062, 2064, 2066, 4000, 4002, 4004, 4006, 4030, 4032, 4034, 4036, 4040, 4042, 4044, 4046, 4050, 4052, 4054, 4056, 4060, 4062, 4064, 4066, 6000}, {13, 17, 31, 37, 71, 73, 79, 97, 107, 113, 149, 157, 167, 179, 199, 311, 337, 347, 359, 389, 701, 709, 733, 739, 743, 751, 761, 769, 907, 937, 941, 953, 967, 971, 983, 991, 1009, 1021, 1031, 1033, 1061, 1069, 1091, 1097, 1103, 1109, 1151, 1153, 1181, 1193}))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube536(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7DHE8RnsCQ8'
        self.title = 'The Centrifuge Problem'
        self.host = ['Holly Krieger']
        self.date = '2018-12-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'requires two numbers'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube537(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_UtCli1SgjI'
        self.title = 'Terrific Toothpick Patterns'
        self.host = ['Neil Sloane']
        self.date = '2018-12-10'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A139250', 'https://oeis.org/A187220', 'https://oeis.org/A161328', 'https://oeis.org/A147562', 'https://oeis.org/A151723']
        self.wiki = None
        self.note = 'sequences'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(result in s for s in ({0, 1, 3, 7, 11, 15, 23, 35, 43, 47, 55, 67, 79, 95, 123, 155, 171, 175, 183, 195, 207, 223, 251, 283, 303, 319, 347, 383, 423, 483, 571, 651, 683, 687, 695, 707, 719, 735, 763, 795, 815, 831, 859, 895, 935, 995, 1083, 1163, 1199, 1215, 1243, 1279, 1319, 1379}, {0, 1, 3, 7, 15, 23, 31, 47, 71, 87, 95, 111, 135, 159, 191, 247, 311, 343, 351, 367, 391, 415, 447, 503, 567, 607, 639, 695, 767, 847, 967, 1143, 1303, 1367, 1375, 1391, 1415, 1439, 1471, 1527, 1591, 1631, 1663, 1719, 1791, 1871, 1991, 2167, 2327, 2399, 2431}, {0, 1, 4, 9, 16, 29, 40, 57, 72, 93, 116, 141, 168, 201, 228, 253, 268, 293, 328, 369, 424, 477, 536, 597, 656, 721, 784, 841, 888, 925, 972, 1037, 1108, 1205, 1300, 1405, 1500, 1589, 1672, 1753, 1840, 1933, 2012, 2085, 2164, 2253, 2360, 2473, 2592, 2705, 2820}, {0, 1, 5, 9, 21, 25, 37, 49, 85, 89, 101, 113, 149, 161, 197, 233, 341, 345, 357, 369, 405, 417, 453, 489, 597, 609, 645, 681, 789, 825, 933, 1041, 1365, 1369, 1381, 1393, 1429, 1441, 1477, 1513, 1621, 1633, 1669, 1705, 1813, 1849, 1957, 2065, 2389, 2401, 2437, 2473}, {0, 1, 7, 13, 31, 37, 55, 85, 127, 133, 151, 181, 235, 289, 331, 409, 499, 505, 523, 553, 607, 661, 715, 817, 967, 1069, 1111, 1189, 1327, 1489, 1603, 1789, 1975, 1981, 1999, 2029, 2083, 2137, 2191, 2293, 2443, 2545, 2599, 2701, 2875, 3097, 3295}))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube538(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0GzhWPj4-cw'
        self.title = 'Introducing the Numberphile Podcast'
        self.host = ['Brady Haran']
        self.date = '2018-12-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube539(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=tP-Ipsat90c'
        self.title = 'Randomness is Random'
        self.host = ['Simon Pampena']
        self.date = '2018-12-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {242830, 1048576, 478520} or is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube540(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yi-s-TTpLxY'
        self.title = 'Divisibility Tricks'
        self.host = ['Tony Padilla']
        self.date = '2019-01-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and any(result % n for n in range(2, 13)) or (is_int(result) and str(int(result))[-1] in {1, 3, 7, 9})])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube541(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=v5KWzOOhZrw'
        self.title = 'The Graceful Tree Problem'
        self.host = ['Gordon Hamilton']
        self.date = '2019-01-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'network of graph nodes'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube542(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=RGQe8waGJ4w'
        self.title = 'The Trapped Knight'
        self.host = ['Neil Sloane']
        self.date = '2019-01-24'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A316667'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 10, 3, 6, 9, 4, 7, 2, 5, 8, 11, 14, 29, 32, 15, 12, 27, 24, 45, 20, 23, 44, 41, 18, 35, 38, 19, 16, 33, 30, 53, 26, 47, 22, 43, 70, 21, 40, 17, 34, 13, 28, 25, 46, 75, 42, 69, 104, 37, 62, 95, 58, 55, 86, 51, 48, 77, 114, 73, 108, 151, 68, 103, 64, 67, 36}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube543(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CCxs-tu8tOU'
        self.title = 'Card Flipping Proof'
        self.host = ['Zandra Vinegar']
        self.date = '2019-02-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0 and is_int(result) and result % 2 == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube544(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6aFcgATW9Mw'
        self.title = 'Heesch Numbers and Tiling'
        self.host = ['Edmund Harriss']
        self.date = '2019-02-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in range(6) or result == math.inf])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube545(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=IKwkX35bcdw'
        self.title = '1010011010'
        self.host = ['Simon Singh']
        self.date = '2019-02-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2048, 2047, 1, 101100101, 357, 1010011010, 666}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube546(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=niaeV_NHh-o'
        self.title = 'A Colorful Unsolved Problem'
        self.host = ['James Grime']
        self.date = '2019-02-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 0.76 < result < 1 or result in {5, 6, 7, 20425}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube547(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5TkIe60y2GI'
        self.title = 'All the Numbers'
        self.host = ['Matt Parker']
        self.date = '2019-03-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube548(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Vv9wpQIGZDw'
        self.title = 'A Million Simulated Seasons'
        self.host = ['Tony Padilla', 'Adam Moss']
        self.date = '2019-03-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {380_000_000, 1_000_000, 114, 44, 161, 50, 896313, 45862, } or (is_int(result) and result >= 33)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube549(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ASoz_NuIvP0'
        self.title = '42 is the new 33'
        self.host = ['Andrew Booker']
        self.date = '2019-03-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {8866128975287528, -8778405442862239, -2736111468807040, 33}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube550(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Wim9WJeDTHQ'
        self.title = "What's special about 277777788888899?"
        self.host = ['Matt Parker']
        self.date = '2019-03-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'what is the distribution of multiplication persistence'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 277777788888899])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube551(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Wim9WJeDTHQ'
        self.title = "What's special about 277777788888899?"
        self.host = ['Matt Parker']
        self.date = '2019-03-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube552(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PsGUEj4w9Cc'
        self.title = 'The Plastic Ratio'
        self.host = ['Ed Harriss']
        self.date = '2019-03-15'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000931'
        self.wiki = 'https://en.wikipedia.org/wiki/Plastic_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 1.32471795724474602596) or is_subsequence_of(context['result'][-3:], (1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, 351, 465, 616, 816, 1081, 1432, 1897, 2513, 3329, 4410, 5842, 7739, 10252, 13581, 17991, 23833, 31572, 41824, 55405, 73396, 97229, 128801, 170625))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube553(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Jwtn5_d2YCs'
        self.title = 'Infinite Series'
        self.host = ['Charlie Fefferman']
        self.date = '2019-04-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube554(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=q6L06pyt9CA'
        self.title = '90,525,801,730 Cannon Balls'
        self.host = ['Matt Parker']
        self.date = '2019-04-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4900, 946, 1045, 5985, 90525801730}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube555(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bRIL9kMJJSc'
        self.title = 'How many ways can circles overlap?'
        self.host = ['Neil Sloane']
        self.date = '2019-04-14'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A250001'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (1, 3, 14, 173, 16951))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube556(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FFftmWSzgmk'
        self.title = "What's so special about the Mandelbrot Set?"
        self.host = ['Ben Sparks']
        self.date = '2019-04-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_complex(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube557(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kjSOSeRZVNg'
        self.title = 'A final game with Elwyn Berlekamp (Amazons)'
        self.host = ['Elwyn Berlekamp']
        self.date = '2019-04-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube558(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Fm0hOex4psA'
        self.title = 'EVERY baby is a ROYAL baby'
        self.host = ['James Grime']
        self.date = '2019-05-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'log' in formula or is_close(result, (1.77, 740_000_000, 2.95, 65_000_000, 25.9, 45.9, 500, 3000, 4000, 7000), 1e-3, method='pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube559(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=z34XhE5oRwo'
        self.title = 'Will your name become extinct?'
        self.host = ['James Grime']
        self.date = '2019-05-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 0 <= result <= 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube560(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=IN1fPtY9jYg'
        self.title = 'Peaceable Queens'
        self.host = ['Neil Sloane']
        self.date = '2019-05-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (0, 0, 1, 2, 4, 5, 7, 9, 12, 14, 17, 21, 24, 28, 32))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube561(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vF_-ob9vseM'
        self.title = 'Game of Cat and Mouse'
        self.host = ['Ben Sparks']
        self.date = '2019-05-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and (1-math.pi/4) <= result <= 0.25])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube562(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fMJflV_GUpU'
        self.title = 'Tribonacci Numbers (and the Rauzy Fractal)'
        self.host = ['Edmund Harriss']
        self.date = '2019-06-03'
        self.source = 'Numberphile'
        self.oeis = 'http://oeis.org/A000073'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601, 334745777, 615693474, 1132436852)) or is_close(result, 1.839286755214161)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube563(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=etMJxB-igrc'
        self.title = "Don't Know (the Van Eck Sequence)"
        self.host = ['Neil Sloane']
        self.date = '2019-06-10'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A181391'
        self.wiki = 'https://en.wikipedia.org/wiki/Van_Eck%27s_sequence'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3, 0, 3, 2, 9, 0, 4, 9, 3, 6, 14, 0, 6, 3, 5, 15, 0, 5, 3, 5, 2, 17, 0, 6, 11, 0, 3, 8, 0, 3, 3, 1, 42, 0, 5, 15, 20, 0, 4, 32, 0, 3, 11, 18, 0, 4, 7, 0, 3, 7, 3, 2, 31, 0, 6, 31, 3, 6, 3, 2, 8, 33, 0, 9, 56, 0, 3, 8, 7, 19, 0, 5, 37, 0, 3, 8, 8, 1))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube564(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=rwiEiGqgetU'
        self.title = 'Necklace Splitting (a lesson for jewel thieves)'
        self.host = ['Noga Alon']
        self.date = '2019-06-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 4, 6} or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube565(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_Wv_qw3nQnI'
        self.title = 'James ❤️ A Card Trick'
        self.host = ['James Grime']
        self.date = '2019-06-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and 1 <= result <= 10) or result in {25}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube566(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xTcvl-kw9fU'
        self.title = 'The Actual Mathematics of Popping Champagne Corks'
        self.host = ['Matt Parker', 'Helen Czerski']
        self.date = '2017-12-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6000, 77, 35, 55, 5, 30, 600, 546, 334, 343, 3.5, 40, 8, 19, 648, 637, 695}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube567(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PLAFNvxDPMw'
        self.title = "Impossible Rubik's Cubes"
        self.host = ['Matt Parker']
        self.date = '2017-12-21'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube568(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fuEAVRc2Im0'
        self.title = 'Dodecaplex: the puzzle from the fourth dimension!'
        self.host = ['Matt Parker', 'Henry Segerman', 'Saul Schleimer']
        self.date = '2018-01-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {120, 4, 5}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube569(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-qqPKKOU-yY'
        self.title = 'How thick is a three-sided coin?'
        self.host = ['Matt Parker', 'Hugh Hunt', 'Jen Rogers']
        self.date = '2018-01-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3**.5 or result in {393, 475, 132, 313, 277, 410} or is_close(result, (333.33, 222.22, 6.826e-42, 1.365e-41), method='pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube570(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LhlqCJjbEa0'
        self.title = 'Calculating π by hand: the Chudnovsky algorithm'
        self.host = ['Matt Parker']
        self.date = '2018-03-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 3.1415926535897961) or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube571(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Bwt5EZEb1Ns'
        self.title = 'How to find a square root'
        self.host = ['Matt Parker']
        self.date = '2018-03-16'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 100.02499687578103 <= result <= 100.025])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube572(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NVUCf8mB1Wg'
        self.title = 'The Tuning Fork Mystery: unexpected vibrations'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2018-03-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube573(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MdZ-vkfZS0I'
        self.title = 'The Tuning Fork Mystery: an unexpected update'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2018-03-27'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube574(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nkXwO5nrimw'
        self.title = 'Inside an Antimatter Factory'
        self.host = ['Matt Parker']
        self.date = '2018-03-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1928, 299792458, I, 1.602176634e-19, -1.602176634e-19, 1931} or is_close(result, 1.054571800e-34, 1e-10) or is_close(result, 1.054571800e-34 * I, 1e-10) or is_close(result, [2.1798722490949962e-18/n**2 for n in range(1, 30)], 1e-10) or is_close(result, 0.0072973525693, 1e-14) or is_close(result, 1.672621898e-27, 1e-10)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube575(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HViA6N3VeHw'
        self.title = 'The Rug Puzzle: how many triangles?'
        self.host = ['Matt Parker']
        self.date = '2018-04-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 720])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube576(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=tQiiaFE1e-Y'
        self.title = 'Psychic Pets: can your pet predict the World Cup results?'
        self.host = ['Matt Parker', 'Steve Mould', 'Django', 'Pablo the Wonder Chameleon']
        self.date = '2018-06-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3, 6} or not is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube577(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=btcVNMA7hYI'
        self.title = 'How many different World Cup results can a team have?'
        self.host = ['Matt Parker']
        self.date = '2018-06-15'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3, 27, 2, 4, 6, 161, 23, 19, 142}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube578(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FF87hs1doiM'
        self.title = 'Why do whole oranges float, but peeled oranges sink?'
        self.host = ['Matt Parker']
        self.date = '2018-07-06'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (246.3, 97.9, 109.4, 231.2, 344.2, 340.6), 1e-2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube579(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=KmjGQBNEayQ'
        self.title = 'Can animals predict the future? Meet Barry the Psychic Labrador!'
        self.host = ['Matt Parker', 'Barry the Psychic Labrador', "Nigel (part of Barry's family)", "Katie (part of Barry's family)"]
        self.date = '2018-07-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {100, 1, 3, 2, 54, 1/54, 133, 38, 43, 52, 14, 38, 12, 11, 15, 5, 16}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube580(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Kpl3BGYtY7g'
        self.title = 'How to detect bank fraud with maths'
        self.host = ['Matt Parker', 'Daniel Chatfield']
        self.date = '2018-07-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube581(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2_NZ1ql8B8Y'
        self.title = 'THE SCUTOID: did scientists discover a new shape?'
        self.host = ['Matt Parker', 'Laura Tallaman', 'Clara Grima']
        self.date = '2018-08-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0, 1, 2, 5, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube582(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4CbPksEl51Q'
        self.title = 'Making a physical Lissajous curve'
        self.host = ['Matt Parker']
        self.date = '2018-09-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'sin' in formula or 'cos' in formula or result in {2, 2.5, 1, 3, 0} or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube583(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=XZGs5Im9f8Q'
        self.title = 'Does daylight savings kill people?'
        self.host = ['Matt Parker']
        self.date = '2018-09-19'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {.24, 24, -.21, -21, 0}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube584(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pSSsZLTMDq0'
        self.title = 'Ordinals vs Cardinals (and how many algebraic numbers are there?)'
        self.host = ['Matt Parker']
        self.date = '2018-09-26'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and result >= 0) or result == math.inf or is_algebraic(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube585(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4ahdOqe5qBk'
        self.title = 'Vector: my new robot maths buddy'
        self.host = ['Matt Parker']
        self.date = '2018-10-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 299_700_000, method='pct') or is_close(result, 0.0035, 1e-4, 'pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube586(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MTmnVBJ9gCI'
        self.title = 'How to estimate a population using statisticians'
        self.host = ['Matt Parker', 'Jen Rogers']
        self.date = '2018-10-15'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {169, 21, 46, 67, 64, 204, 475}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube587(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pgyI8aPctaI'
        self.title = 'Stand-up comedy routine using a live spherical camera'
        self.host = ['Matt Parker', 'Steve Mould', 'Helen Arney']
        self.date = '2018-11-06'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1 <= result <= 6])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube588(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=UqtaKJQM_GM'
        self.title = 'The equations behind my live spherical footage'
        self.host = ['Matt Parker', 'Aaron Montag', 'Ken Farquhar']
        self.date = '2018-11-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.inf or is_complex(result) or any(f in formula for f in ('^', 'mod', 'log'))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube589(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BnnmA2klBN8'
        self.title = 'Infinite DVD unboxing video: Festival of the Spoken Nerd'
        self.host = ['Matt Parker']
        self.date = '2018-12-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 4 or result == math.inf])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube590(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mrgN-tvg53I'
        self.title = 'How many calendars are there?'
        self.host = ['Matt Parker']
        self.date = '2018-12-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2018, 2561, 14, 1974, 1985, 2019, 2020, 1992, 2048, 7, 400, 20871*7, 20000000, 2000}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube591(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xEh4OaXeexU'
        self.title = '2019 facts in 2 mins 19 seconds'
        self.host = ['Matt Parker']
        self.date = '2018-12-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2019, 2*60+19}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube592(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NinrTW1Bx2Y'
        self.title = 'Happy Thirdsday: finding a third using only halves'
        self.host = ['Matt Parker']
        self.date = '2019-01-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1/3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube593(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OZzIvl1tbPo'
        self.title = 'Superpermutations: the maths problem solved by 4chan'
        self.host = ['Matt Parker', 'Robin Houston']
        self.date = '2019-01-28'
        self.source = 'standupmaths'
        self.oeis = 'http://oeis.org/A007489'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], (0, 1, 3, 9, 33, 153, 872))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube594(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OZzIvl1tbPo'
        self.title = 'Superpermutations: the maths problem solved by 4chan'
        self.host = ['Matt Parker', 'Robin Houston']
        self.date = '2019-01-28'
        self.source = 'standupmaths'
        self.oeis = 'http://oeis.org/A007489'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) >= 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube595(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0X_Hqb7qkW4'
        self.title = 'Bad Rounding: ⌊Trump vs Obamacare⌋'
        self.host = ['Matt Parker']
        self.date = '2019-02-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 3, 3.49-3) or is_close(result, 1, 1-0.77) or is_close(result, 5, 5-4.97)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube596(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=IoYm8lcJQ0o'
        self.title = 'How fast is a bullet? [featuring: pendulum calculation]'
        self.host = ['Matt Parker', 'Hugh Hunt', 'Maria Kettle', 'Katherine Fleck']
        self.date = '2019-02-22'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {26, 95, 2.6, 1.9, 9.8, 8.6, 324.1, 2.84, 9.5, 343, 323.4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube597(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HYgqvapH7ak'
        self.title = 'Humble Pi: plane wrong'
        self.host = ['Matt Parker']
        self.date = '2019-02-26'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'binary'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4294967295, 2147483647, 0} or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube598(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-g3iY0dMN_0'
        self.title = 'Humble Pi: Los Angeles crime and Null Island'
        self.host = ['Matt Parker']
        self.date = '2019-03-06'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result) or result == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube599(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=S26_O2B8h8k'
        self.title = 'Pi Day 2019: calculating π with a balancing beam'
        self.host = ['Matt Parker']
        self.date = '2019-03-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {math.pi, math.pi**2 / 6, 550, 6.480909, 1.620, 3.11791} or is_close(result, math.pi, math.pi - 3.12)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube600(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_tpNuulTeSQ'
        self.title = 'New Superpermutations Discovered!'
        self.host = ['Matt Parker', 'Robin Houston', 'James Grime', 'Helen Arney']
        self.date = '2019-03-11'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {5907, 5906}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube601(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aes29YXIrRk'
        self.title = 'Live Q + A with Matt Parker'
        self.host = ['Matt Parker']
        self.date = '2019-03-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in range(11) or result in {5495, 340}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube602(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7GgLSnQ48os'
        self.title = 'Bayesian Statistics with Hannah Fry'
        self.host = ['Matt Parker', 'Hannah Fry']
        self.date = '2019-03-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1731, 1761, 1702, 5}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube603(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=94WaOl2Actw'
        self.title = 'When Buildings Wobble: with Paul Shepherd'
        self.host = ['Matt Parker', 'Paul Shepherd']
        self.date = '2019-04-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {38}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube604(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LkIK8f4yvOU'
        self.title = 'The Difference of Two Squares'
        self.host = ['Matt Parker', 'James Grime']
        self.date = '2019-05-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: not is_error(result) and (is_real(result) and (result % 2 == 1 or result % 4 == 0))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube605(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=iyz7dSnZItw'
        self.title = "Why didn't GPS crash?"
        self.host = ['Matt Parker']
        self.date = '2019-04-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1023, 50.67833, 1.138683, 8192}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube606(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=b-Fa6HtvGtQ'
        self.title = 'Recursive PowerPoint Presentations [Gone Fractal!]'
        self.host = ['Matt Parker', 'Steve Mould']
        self.date = '2019-05-17'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_subsequence_of(context['result'][-3:], FIBONACCI_NUMBERS)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube607(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=waqDoeQ0Ijw'
        self.title = 'Calculator Number Trick: rectangle patterns'
        self.host = ['Matt Parker']
        self.date = '2019-05-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1111 <= result <= 9999 and result % 11 == 0 and '0' not in str(int(result))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube608(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OcTMBrUutfk'
        self.title = "What's the story with log(1 + 2 + 3)?"
        self.host = ['Matt Parker']
        self.date = '2019-06-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {6, 101*1.01, 4, 1.618}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube609(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OcTMBrUutfk'
        self.title = "What's the story with log(1 + 2 + 3)?"
        self.host = ['Matt Parker']
        self.date = '2019-06-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 4])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube610(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=eYfpSAxGakI'
        self.title = 'The Dehn Invariant'
        self.host = ['Daniel Litt']
        self.date = '2019-07-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube611(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0mXz-NP-raY'
        self.title = 'Frieze Patterns'
        self.host = ['Sergei Tabachnikov']
        self.date = '2019-08-06'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A000108'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and int(result) in {1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452, 18367353072152, 69533550916004, 263747951750360, 1002242216651368, 3814986502092304}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube612(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pAMgUB51XZA'
        self.title = 'Amazing Graphs'
        self.host = ['Neil Sloane']
        self.date = '2019-08-08'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A133058', 'https://oeis.org/A265326']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (int(result) in {1, 1, 4, 8, 2, 8, 4, 12, 3, 1, 12, 24, 2, 16, 8, 24, 3, 21, 7, 27, 48, 16, 8, 32, 4, 30, 15, 5, 34, 64, 32, 64, 2, 36, 18, 54, 3, 41, 80, 120, 3, 45, 15, 59, 104, 150, 75, 123, 41, 91, 142, 194, 97, 151, 206, 262, 131, 189, 248, 308, 77, 139, 202, 266, 133, 199, 266, 334, 167} or result == 638 or result in {1, 0, 0, 0, -2, 2, 0, -6, -6, 6, 0, -4, 4, -10, -14, 10, 4, 14, -30, -42, 0, -42, -18, 12, 30, 18, -12, 0, 18, 42, 0, -62, -8, -70, -20, -82, -28, -34, -62, -8, -26, 8, -62, 62, 34, -28, 8, -28, 28, 62, 82, -8, 98, 28, 0, -186, -84, -210, -60})])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube613(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=o8c4uYnnNnc'
        self.title = 'Amazing Graphs II (including Star Wars)'
        self.host = ['Neil Sloane']
        self.date = '2019-08-14'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A117966', 'https://oeis.org/A063543', 'https://oeis.org/A229037', 'https://oeis.org/A123456', 'https://oeis.org/A118131']
        self.wiki = None
        self.note = 'interesting research opportunity'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube614(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=j0o-pMIR8uk'
        self.title = 'Amazing Graphs III'
        self.host = ['Neil Sloane']
        self.date = '2019-08-22'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A002487', 'https://oeis.org/A005185', 'https://oeis.org/A279125']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (int(result) in {0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3, 8, 5, 7, 2, 7, 5, 8, 3, 7, 4, 5, 1, 6, 5, 9, 4, 11, 7, 10, 3, 11, 8, 13, 5, 12, 7, 9, 2, 9, 7, 12, 5, 13, 8, 11, 3, 10, 7, 11, 4, 9, 5, 6, 1, 7, 6, 11, 5, 14, 9, 13, 4, 15, 11, 18, 7, 17, 10, 13, 3, 14, 11, 19, 8, 21, 13, 18, 5, 17, 12, 19} or int(result) in {1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8, 8, 8, 10, 9, 10, 11, 11, 12, 12, 12, 12, 16, 14, 14, 16, 16, 16, 16, 20, 17, 17, 20, 21, 19, 20, 22, 21, 22, 23, 23, 24, 24, 24, 24, 24, 32, 24, 25, 30, 28, 26, 30, 30, 28, 32, 30, 32, 32, 32, 32, 40, 33, 31, 38, 35, 33, 39, 40, 37, 38, 40, 39} or int(result) in {0, 0, 1, 0, 2, 3, 4, 0, 3, 2, 5, 1, 6, 7, 8, 0, 7, 6, 9, 5, 10, 11, 12, 4, 13, 14, 15, 16, 17, 18, 19, 0, 11, 10, 16, 9, 14, 13, 20, 12, 21, 22, 23, 24, 25, 26, 27, 1, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 0, 18, 17, 24, 15, 22, 21, 35, 9})])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube615(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ERBVFcutl3M'
        self.title = 'Navier-Stokes Equations'
        self.host = ['Tom Crawford']
        self.date = '2019-08-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube616(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wtIhVwPruwY'
        self.title = 'Reynolds Number'
        self.host = ['Tom Crawford']
        self.date = '2019-09-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Reynolds_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube617(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=zyG8Vlw5aAw'
        self.title = 'The Mystery of 42 is Solved'
        self.host = ['Andrew Booker']
        self.date = '2019-09-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {-80538738812075974, 80435758145817515, 12602123297335631, 42, 3, 114, 165, 390, 579, 627, 633, 732, 906, 921, 975}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube618(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=GXhzZAem7k0'
        self.title = '3 as the sum of the 3 cubes'
        self.host = ['Andrew Booker']
        self.date = '2019-09-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {3, 1, 4, -5, 569939821221962380720, -569936821113563493509, -472715493453327032, 114, 906, -74924259395610397, 72054089679353378, 35961979615356503, 165, 390, 579, 627, 633, 732, 921, 975}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube619(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5mGh0r3zC6Y'
        self.title = 'Where Does River Water Go?'
        self.host = ['Tom Crawford']
        self.date = '2019-10-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube620(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7H4lDi79YY8'
        self.title = 'The Forgotten Flexagon'
        self.host = ['Matt Parker']
        self.date = '2019-10-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 6, 4, 1, 2, 3, 4, 5, 6, 7}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube621(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0X9DYRLmTNY'
        self.title = "TREE vs Graham's Number"
        self.host = ['Tony Padilla']
        self.date = '2019-10-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == GRAHAMS_NUMBER or (is_real(result) and result > sys.float_info.max)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube622(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xBkTIp6ajAg'
        self.title = 'Planar Graphs'
        self.host = ['Maria Chudnovsky']
        self.date = '2019-11-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube623(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nWQwrU1qUrc'
        self.title = 'Are odd-numbered mobius-loop cogs possible?'
        self.host = ['Matt Parker']
        self.date = '2019-07-17'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 3 and int(result) % 2 == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube624(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MPGMfCk4VpA'
        self.title = 'Curvahedra: how many faces make a polyhedron'
        self.host = ['Matt Parker', 'Edmund Harriss']
        self.date = '2019-07-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {180, 60, 72, 216, 36, 20, 90, 120, 0}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube625(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=h9FZgaPdIuY'
        self.title = 'Eclipses can be approximated the same way as π. [ONE TAKE!]'
        self.host = ['Matt Parker']
        self.date = '2019-07-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.pi, 29.53058885, 27.21222082, 2.170391682)) or is_subsequence_of([2, 5, 1, 6, 1, 1, 1, 1, 11], context['result'])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube626(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=x5h3yTxeCew'
        self.title = 'How to mathematically hang a picture (badly).'
        self.host = ['Matt Parker', 'Steve Mould']
        self.date = '2019-08-02'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube627(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2SgG99QKLFE'
        self.title = 'Can we film a stroboscopic helicopter?'
        self.host = ['Matt Parker', 'Polina Harkin']
        self.date = '2019-08-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {535, 25, 26, 27} or is_close(result, 8.917)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube628(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ZLTyX4zL2Fc'
        self.title = 'Can you solve The Frog Problem?'
        self.host = ['Matt Parker', 'Timandra Harkness', 'Bec Hill', 'Rob West']
        self.date = '2019-09-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and 1 <= result <= 10) or is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube629(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=b9OEuhdM6t8'
        self.title = 'Is the London Underground knotted?'
        self.host = ['Matt Parker', 'Sabetta Matsumoto', 'Henry Segerman', 'Geoff Marshall', 'Vicki Pipe']
        self.date = '2019-09-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {32, 19, 4, -12, -13, 6}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube630(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1K-uEwD0OTg'
        self.title = 'How to make a fold-and-cut bat for Halloween!'
        self.host = ['Matt Parker']
        self.date = '2019-10-21'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 6])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube631(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=a1DUUnhk3uE'
        self.title = 'The unbelievable solution to the 100 prisoner puzzle.'
        self.host = ['Matt Parker', 'Alex Bellos', 'Matthew Scroggs']
        self.date = '2019-11-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and 1 <= result <= 10) or result in {0.5, 1/1024, 1285920/3628800, 3628800, 1285920, 0.31}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube632(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=48QQXpbTlVM'
        self.title = 'Help, our train home is making 9 quintillion stops.'
        self.host = ['Matt Parker']
        self.date = '2019-11-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {9_223_372_036_854_775_798, 9e18} or is_close(result, 2**63, 10) or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube633(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6_yU9eJ0NxA'
        self.title = 'Darts in Higher Dimensions (with 3blue1brown)'
        self.host = ['Grant Sanderson']
        self.date = '2019-11-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'game, multiple dimensions'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in ((math.pi/4)**n/math.factorial(n) for n in range(1, 20)) or is_close(result, math.e**(math.pi/4))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube634(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=eeoBCS7IEqs'
        self.title = 'Primes without a 7'
        self.host = ['James Maynard']
        self.date = '2019-11-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and is_prime(result) and '7' not in str(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube635(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dNxyFtqcNss'
        self.title = 'The Archimedes Number'
        self.host = ['Alex Bellos']
        self.date = '2019-11-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {22, 50_389_082, 51_285_802_909_803, 206545} or (is_int(result) and str(result).startswith('766'))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube636(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0JOoTWO2L_4'
        self.title = 'Taking a Turkey’s Temperature'
        self.host = ['Cliff Stoll']
        self.date = '2019-11-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 104])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube637(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1LoSV1sjZFI'
        self.title = 'Approximating Irrational Numbers (Duffin-Schaeffer Conjecture)'
        self.host = ['James Maynard']
        self.date = '2019-12-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_irrational(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube638(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0rxghexCKj8'
        self.title = 'Checking the exact angle of parking bays.'
        self.host = ['Matt Parker']
        self.date = '2019-12-13'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {60, 5.38, 5.42, 5.95, 65.2, 2.5, 24.8} or (is_real(result) and 60 <= result <= 60.4925)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube639(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=J4PO7NbdKXg'
        self.title = 'Synchronising Metronomes in a Spreadsheet'
        self.host = ['Matt Parker']
        self.date = '2019-12-27'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (len(context['result']) >= 2 and result == context['result'][-2]) or 'sin' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube640(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=N92w4e-hrA4'
        self.title = 'A Fascinating Thing about Fractions'
        self.host = ['Holly Krieger']
        self.date = '2019-12-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0, 1, 2, 3, 1/2, -7/4, -29/16, 5/4, -1/4}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube641(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Tnu_Ws7Llo4'
        self.title = 'A Breakthrough in Graph Theory'
        self.host = ['Erica Klarreich']
        self.date = '2019-12-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'tensors'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4**100, 4**10_000}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube642(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=__UlMppZZgs'
        self.title = 'Pi Million Subscribers'
        self.host = ['Bobak Ferdowsi', 'Henry Reich', 'Dave Brown', 'Alex Dainis', 'Bobby Wilson', 'Matt Parker', 'Captain Disillusion', 'Jenny Hammerton', 'Jason Davison', 'Martyn Poliakoff', 'John Green', 'Bethany Palumbo', 'James Maynard', 'Helen Arney', 'Katie Mack', 'Patreon supporters', 'Alex Bellos', 'Scott Manley', 'Pete McPartlan', 'Grant Sanderson', 'Joe Hanson', 'Colin Wright', 'Pete Watts', 'Hannah Fry', 'Sarah Wiseman', 'Simon Clark', 'Emily Calandrelli', 'Matt Whitman', 'Phil Moriarty', 'James Hennessy', 'Steve Mould', 'Dianna Cowern', 'Carlo Séquin', 'Emily Graslie', 'Tony Padilla', 'Alex from LowSpecGamer', 'Cliff Stoll', 'Jabrils', 'Kevin Lieber', 'Ed Copeland', 'Johnny Ball', 'Sean Riley', 'Kurzgesagt', 'Ken Ribet', 'Jonathan Tallant', 'Mike Pound', 'CGP Grey', 'Ron Graham', 'Stephanie Kent', 'Sabetta Matsumoto', 'Brian McManus', 'Seb (Dinosaur)', 'Maggie Lieu', 'Destin Sandlin', 'Caleb Ashley', 'John Urschel', 'Federico Ardila', 'Tom Crawford', 'Vi Hart', 'Steve Bagley', 'Ria Symonds', 'J Willgoose Esq', 'Hank Green', 'David Eisenbud', 'Daniel Erman', 'Creepy Face Puppet', 'Keith Moore', 'Bobby Seagull', 'Adam Savage', 'Steven Strogatz', 'Simon Singh', 'Michael Stevens', 'Neil Sloane', 'Rob Eastaway', 'Greg Foot', 'Jake Roper', 'Zvezdelina Stankova', 'Stan Muller', 'Susan Okereke', 'Dabchick via Barnbaby Dixon', 'Lê Nguyên Hoang', 'Mark Rober', 'Dave Brailsford', 'Holly Krieger', 'Ted Hamilton', 'Maddie Moate', 'Henry Segerman', 'Laura Outterside', 'James Grime', 'Tim Hein', 'Bruce Benamran', 'Andrew Booker', 'Calvin Lin', 'Rob Miles', 'Zandra Vinegar', 'Derek Muller', 'Daniel Litt', 'Becky Smethurst', 'Mike Merrifield', 'Brady Haran', 'Simon Pampena', 'Logan Smalley', 'Alan Stewart', 'Tom Scott', 'Katie Steckles', 'Kylie Pentelow', 'Ben Sparks', 'Edward Frenkel', 'Casandra Monroe']
        self.date = '2019-12-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3141592])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube643(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Wrj1Kl6CHIQ'
        self.title = 'Counting Outtakes (from our Pi Million video)'
        self.host = ['Bobak Ferdowsi', 'Henry Reich', 'Dave Brown', 'Alex Dainis', 'Bobby Wilson', 'Matt Parker', 'Captain Disillusion', 'Jenny Hammerton', 'Jason Davison', 'Martyn Poliakoff', 'John Green', 'Bethany Palumbo', 'James Maynard', 'Helen Arney', 'Katie Mack', 'Patreon supporters', 'Alex Bellos', 'Scott Manley', 'Pete McPartlan', 'Grant Sanderson', 'Joe Hanson', 'Colin Wright', 'Pete Watts', 'Hannah Fry', 'Sarah Wiseman', 'Simon Clark', 'Emily Calandrelli', 'Matt Whitman', 'Phil Moriarty', 'James Hennessy', 'Steve Mould', 'Dianna Cowern', 'Carlo Séquin', 'Emily Graslie', 'Tony Padilla', 'Alex from LowSpecGamer', 'Cliff Stoll', 'Jabrils', 'Kevin Lieber', 'Ed Copeland', 'Johnny Ball', 'Sean Riley', 'Kurzgesagt', 'Ken Ribet', 'Jonathan Tallant', 'Mike Pound', 'CGP Grey', 'Ron Graham', 'Stephanie Kent', 'Sabetta Matsumoto', 'Brian McManus', 'Seb (Dinosaur)', 'Maggie Lieu', 'Destin Sandlin', 'Caleb Ashley', 'John Urschel', 'Federico Ardila', 'Tom Crawford', 'Vi Hart', 'Steve Bagley', 'Ria Symonds', 'J Willgoose Esq', 'Hank Green', 'David Eisenbud', 'Daniel Erman', 'Creepy Face Puppet', 'Keith Moore', 'Bobby Seagull', 'Adam Savage', 'Steven Strogatz', 'Simon Singh', 'Michael Stevens', 'Neil Sloane', 'Rob Eastaway', 'Greg Foot', 'Jake Roper', 'Zvezdelina Stankova', 'Stan Muller', 'Susan Okereke', 'Dabchick via Barnbaby Dixon', 'Lê Nguyên Hoang', 'Mark Rober', 'Dave Brailsford', 'Holly Krieger', 'Ted Hamilton', 'Maddie Moate', 'Henry Segerman', 'Laura Outterside', 'James Grime', 'Tim Hein', 'Bruce Benamran', 'Andrew Booker', 'Calvin Lin', 'Rob Miles', 'Zandra Vinegar', 'Derek Muller', 'Daniel Litt', 'Becky Smethurst', 'Mike Merrifield', 'Brady Haran', 'Simon Pampena', 'Logan Smalley', 'Alan Stewart', 'Tom Scott', 'Katie Steckles', 'Kylie Pentelow', 'Ben Sparks', 'Edward Frenkel', 'Casandra Monroe']
        self.date = '2019-12-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in range(10) or is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube644(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=K54ildEW9-Q'
        self.title = 'How to keep an open secret with mathematics.'
        self.host = ['Matt Parker']
        self.date = '2019-12-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {19211319} or (is_int(result) and 0 <= result <= 100_000_000)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube645(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SPQRNmXVP8s'
        self.title = 'Visiting every Platform Zero in the UK in one day!'
        self.host = ['Matt Parker', 'Geoff Marshall']
        self.date = '2020-01-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube646(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NbiveCNBOxk'
        self.title = 'Does The Average Person Exist?'
        self.host = ['Matt Parker']
        self.date = '2020-01-17'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'average'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {250, 37, 2, 9, 6, 3, 23401892, 400, 132, 4063, 14, 2.5, 143, 0.3, 1055, 302, 143, 73, 28, 12, 6, 3, 2, 0}, lambda formula, result, context: is_real(result) and (0.25 <= result <= 0.3 or 25 <= result <= 30)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube647(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=iwzzv1biHv8'
        self.title = 'The Datasaurus Dozen'
        self.host = ['Matt Parker', 'Justin Matejka']
        self.date = '2020-01-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'average'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and (5_929_040 <= result <= 6_000_000 or 39.7 <= result <= 40), lambda formula, result, context: any(is_close(result, v, 1e-2) for v in [54.26, 47.83, 16.76, 26.93, -0.06] + [54.28, 46.04, 20.38, 22.04, 0.33])])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube648(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yb2zkxHDfUE'
        self.title = 'When Spreadsheets Attack!'
        self.host = ['Matt Parker']
        self.date = '2020-01-24'
        self.source = 'standupmaths'
        self.oeis = 'http://oeis.org/A262222'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {25_000_000, 400_000, 6_000_000_000, 15_770, 113.4, 41, 5.1, 175, 6191, 1286, 6650, 42.2, 0.422, 9120, 24, 0.24, 755, 83273, 1414042559, 3597, 35175, 987, 704}, lambda formula, result, context: is_real(result) and (0.9 <= result <= 1 or 90 <= result <= 100), lambda formula, result, context: result in {480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube649(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4fE_sXZjxng'
        self.title = 'Why 02/02/2020 is the most palindromic date ever.'
        self.host = ['Matt Parker']
        self.date = '2020-02-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {20200202, 2022020, 8311380, 10022001, 9222290, 10033001, 36, 29111192, 10022001, 29122192, 10033001, 60, 3033030, 30300303, 33, 333, 1022, 2010, 2020, 2190, 2210, 9021, 9221, 37.5, 0.375}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube650(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=uNPDrLhXC9k'
        self.title = 'Will a falling pencil hit the table? We do the maths!'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2020-02-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (2.2789, 130))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube651(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CKl1B8y4qXw'
        self.title = 'Calculating π by hand the Isaac Newton way: Pi Day 2020'
        self.host = ['Matt Parker', 'Ben Sparks', 'Deanna Judd', 'Max Hughes', 'Zoe Griffiths']
        self.date = '2020-03-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, 3.141591678589793935225)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube652(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6egeUxIEQnM'
        self.title = 'Why do people keep getting this wrong‽'
        self.host = ['Matt Parker']
        self.date = '2020-03-24'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {500_000_000, 327_000_000, 1.529, 317_000_000, 360_000_000}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube653(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=T29dydI97zY'
        self.title = 'MPMP: Can you spin the table?'
        self.host = ['Matt Parker']
        self.date = '2020-03-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 7 or (is_int(result) and 2 <= result <= 7)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube654(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ER1a6jgW1Gs'
        self.title = 'Why is the Apple Calendar so broken?'
        self.host = ['Matt Parker']
        self.date = '2020-04-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1849, 1848, 200, 199}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube655(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=JaXo_i3ktwM'
        self.title = 'MPMP: Can you play Scrabble over a video call?'
        self.host = ['Matt Parker', 'Vicki Pipe']
        self.date = '2020-04-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'random'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result) or is_close(result, (5.9604827, 6.6008077, 4.3016657, 0.2712588, 0.0184608, 0.0012537), 1e-7) or result in {100, 2, 3} or is_close(result, [0.2460931405] +[float(f'0.{i}451811228') for i in range(1, 4)], 1e-10)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube656(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=oCMVUROty0g'
        self.title = 'Can you crack the face-down card game?'
        self.host = ['Matt Parker', 'Matt Parker']
        self.date = '2020-04-15'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {4, 8, 1}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube657(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vBPFaM-0pI8'
        self.title = "The Parker Machine: it's 80% accurate."
        self.host = ['Matt Parker', 'Hannah Fry']
        self.date = '2020-04-24'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result) or result in {100, 5, 0.05, 95, 0.95, 80, 0.8, 20, 0.2}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube658(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=YBnBAzrWeF0'
        self.title = 'The 1890 US Census and the history of punchcard computing [feat. Grant of 3blue1brown fame]'
        self.host = ['Matt Parker', 'Grant Sanderson']
        self.date = '2020-04-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1890, 10, 40, 7000, 1896, 1911, 10, 1000, 1401}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube659(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MrEECYAXRjs'
        self.title = 'Are Matt and James anti-psychic?'
        self.host = ['Matt Parker', 'James Grime']
        self.date = '2020-05-18'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'random'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {0, 10, 52, 1/3_000_000} or is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube660(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=G9_l8QASobI'
        self.title = 'A New Discovery about Dodecahedrons - Numberphile'
        self.host = ['Jayadev Athreya']
        self.date = '2020-01-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {12, 0, 10, 81, 31, math.inf}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube661(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kE3OuzlkUnU'
        self.title = 'Colouring Numbers - Numberphile'
        self.host = ['Timothy Gowers']
        self.date = '2020-01-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube662(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=uvMGZb0Suyc'
        self.title = 'A Prime Surprise (Mertens Conjecture) - Numberphile'
        self.host = ['Holly Krieger']
        self.date = '2020-01-23'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A002321', 'https://oeis.org/A084237']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube663(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=UIjeCKPHbso'
        self.title = 'Superhero Triangles - Numberphile'
        self.host = ['James Grime']
        self.date = '2020-01-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {5, 12, 13, 30, 6, 8, 10, 24, 9, 10, 17, 36, 7, 15, 20, 42, 6, 25, 29, 60}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube664(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HJ_PP5rqLg0'
        self.title = 'Russian Multiplication - Numberphile'
        self.host = ['Johnny Ball']
        self.date = '2020-02-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'binary numbers'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_int(result) and result % 2 != 0) or '*' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube665(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=bJOuzqu3MUQ'
        self.title = "A Miraculous Proof (Ptolemy's Theorem) - Numberphile"
        self.host = ['Zvezdelina Stankova']
        self.date = '2020-02-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube666(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=o3QBgkQi_HA'
        self.title = 'Pentagons and the Golden Ratio - Numberphile'
        self.host = ['Zvezdelina Stankova']
        self.date = '2020-02-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: (is_real(result) and result > 0) or result == GOLDEN_RATIO])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube667(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=feUPkMGACtk'
        self.title = 'Tentacles Akimbo (with Cliff Stoll) - Numberphile'
        self.host = ['Cliff Stoll']
        self.date = '2020-02-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 2 or result == 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube668(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=W20aT14t8Pw'
        self.title = 'Strings and Loops within Pi - Numberphile'
        self.host = ['Tom Crawford']
        self.date = '2020-02-20'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A057680', 'https://oeis.org/A064810']
        self.wiki = None
        self.note = 'how does it behave in different bases?'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: len(context['result']) == result or len(context['result'])-1 == result or is_close(result, math.pi) or result in {1, 16470, 44899, 79873884, 711939213, 36541622473, 45677255610, 62644957128, 656430109694} or result in {6, 27, 13598, 43611, 24643510, 71683711, 78714901, 268561754, 4261759184, 82638677082, 548535559133} or result in [169, 40, 70, 96, 180, 3664, 24717, 15492, 84198, 65489, 3725, 16974, 41702, 3788, 5757, 1958, 14609, 62892, 44745, 9385] or result in [211, 93, 14, 1]])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube669(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=f-Pe1ZMJEXk'
        self.title = 'The 17-Klein Bottle - Numberphile'
        self.host = ['Cliff Stoll']
        self.date = '2020-02-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and result % 2 == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube670(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dfhiVaJj9UY'
        self.title = 'How to Fill a Klein Bottle - Numberphile'
        self.host = ['Cliff Stoll']
        self.date = '2020-03-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result >= 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube671(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ELA8gNNMHoU'
        self.title = 'Random Fibonacci Numbers - Numberphile'
        self.host = ['James Grime']
        self.date = '2020-03-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'random'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result) or is_close(result, 1.1319882487943)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube672(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9VVPBS_flOI'
        self.title = 'Mesolabe Compass and Square Roots - Numberphile'
        self.host = ['Johnny Ball']
        self.date = '2020-03-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '*' in formula or '/' in formula or 'sqrt' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube673(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9ptyprXFPX0'
        self.title = '3 Ways to Draw Squares Inside Triangles - Numberphile'
        self.host = ['Calvin Lin']
        self.date = '2020-03-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result >= 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube674(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=k6nLfCbAzgo'
        self.title = 'The Coronavirus Curve - Numberphile'
        self.host = ['Ben Sparks']
        self.date = '2020-03-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 0 <= result <= 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube675(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mTvKQYTV0Yw'
        self.title = 'Mathematics and Coronavirus - Numberphile'
        self.host = ['Kit Yates']
        self.date = '2020-03-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube676(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xyVl-tcB8pI'
        self.title = 'Impossible Squares - Numberphile'
        self.host = ['Ben Sparks']
        self.date = '2020-04-04'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A001481', 'https://oeis.org/A022544']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and any((len(list(g))%2 == 1 and k%4 == 3) for k, g in itertools.groupby(factors(result, 'prime')))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube677(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=X3l0fPHZja8'
        self.title = "The Daddy of Big Numbers (Rayo's Number) - Numberphile"
        self.host = ['Tony Padilla']
        self.date = '2020-04-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'technically, there is a value...'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube678(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=YI1WqYKHi78'
        self.title = 'Why is this Puzzle Impossible? - Numberphile'
        self.host = ['Steven Bradlow']
        self.date = '2020-04-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in range(1, 17)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube679(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=qu04xLNrk94'
        self.title = 'Euler Squares - Numberphile'
        self.host = ['James Grime']
        self.date = '2020-05-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 9408 or result in {2, 6, 10, 14, 18, 22}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube680(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=n2Kp3toDJ9c'
        self.title = "Lewis Carroll's Pillow Problem - Numberphile"
        self.host = ['Alex Bellos']
        self.date = '2020-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1/3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube681(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wTUSz-HSaBg'
        self.title = 'Matrix Factorization - Numberphile'
        self.host = ['David Eisenbud']
        self.date = '2020-05-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'matrix'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube682(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=IMY2_yzDm9I'
        self.title = 'A Surprising Pi and 5 - Numberphile'
        self.host = ['Ben Sparks']
        self.date = '2020-05-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(is_close(result, math.pi * 10**-i, 10**-(i+2)) for i in range(1, 30)), lambda formula, result, context: is_int(result) and all(c == '5' for c in str(int(result))), lambda formula, result, context: is_real(result) and 0 < result < 1 and is_int(1/result) and all(c == '5' for c in str(int(1/result)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube683(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ghxQA3vvhsk'
        self.title = 'Complex Fibonacci Numbers?'
        self.host = ['Matt Parker']
        self.date = '2020-07-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_complex(result), lambda formula, result, context: is_real(result) and result in (abs(v) for v in FIBONACCI_NUMBERS)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube684(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=as7Gkm7Y7h4'
        self.title = 'The almost impossible chessboard puzzle'
        self.host = ['Matt Parker', 'Grant Sanderson']
        self.date = '2020-07-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'binary'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0 and is_int(math.log2(result))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube685(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=7LKy3lrkTRA'
        self.title = "Why do calculators get this wrong? (We don't know!)"
        self.host = ['Matt Parker']
        self.date = '2020-07-16'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'Farey addition'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and (11**6 / 13 <= result <= 156158413/3600 * math.pi) and (not result in (17**5 / 11, 11**6 / 17, 19**9 / 2**3, 5**9 / 3, 7**9 / 19, 13**5 / 7, 21**6 / 5, 23**9 / 5**4))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube686(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l51LcwHOW7s'
        self.title = 'Ellipsoids and The Bizarre Behaviour of Rotating Bodies'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2020-07-24'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube687(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PtKhbbcc1Rc'
        self.title = 'Does "land area" assume a country is perfectly flat?'
        self.host = ['Matt Parker']
        self.date = '2020-08-19'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {243610, 242495, 7688287, 245415, 246029, 246653, 247719, math.inf}, lambda formula, result, context: is_close(result, (0.25, 0.50, 0.0025, 0.0050, 0.94, 0.0094))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube688(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=A7eJb8n8zAw'
        self.title = 'What is the biggest tangent of a prime?'
        self.host = ['Matt Parker']
        self.date = '2020-08-19'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1_169_809_367_327_212_570_704_813_632_106_852_886_389_036_911, 1, 11, 33, 52174, 260515, 573204, 37362253, 42781604, 122925461}, lambda formula, result, context: is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube689(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=esC4HB-AjgI'
        self.title = 'Landmark Numbers and Bad Number Analogies'
        self.host = ['Matt Parker', 'Tim Harford']
        self.date = '2020-08-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'units'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (1_000_000_000 / 3, 2/3 * 100_000_000, 365 * 1_000_000_000 / 3, 365 * 2/3 * 100_000_000, 381, 30_000, 1_000_000, 1_000_000_000, 1_000_000_000_000), method='pct')])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube690(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PooFvQEN4n8'
        self.title = 'Orbital Maths at NASA with Chris Hadfield'
        self.host = ['Matt Parker', 'Chris Hadfield']
        self.date = '2020-08-28'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {92, 17_500, 28000, 5, 8, 6420}, lambda formula, result, context: is_close(result, (9, 8000))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube691(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=V_brZ-KWY3g'
        self.title = 'The Rocket Equation: Mathematician vs Astronaut'
        self.host = ['Matt Parker']
        self.date = '2020-09-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (8000, -3500, 11, 0.11), method='pct'), lambda formula, result, context: is_real(result) and (10 <= result <= 15 or 0.10 <= result <= 0.15), lambda formula, result, context: is_close(result, (200_000, 90_000))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube692(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=5nW3nJhBHL0'
        self.title = 'Why is there no equation for the perimeter of an ellipse‽'
        self.host = ['Matt Parker']
        self.date = '2020-09-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'That last tuple of numbers from the first test comes from `(Fraction(int(double_factorial(2*n - 3)**2), (2**n * math.factorial(n))**2) for n in range(0, 11))`'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {2, 1/2, 3, 4, 53, 53/3, 717/35, 717, 35, 269, 667, 371, 6, 5, 0.75, 1.2} or is_close(result, math.pi) or (is_int(result) and int(result) in (1, 64, 256, 25, 16384, 49, 65536, 441, 1048576, 1089, 4194304, 184041, 1073741824, 511225, 4294967296, 5909761, 68719476736)), lambda formula, result, context: result in (46, 1017, 35085)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube693(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Z4oy6mnkyW4'
        self.title = 'General Relativity: Top 05 Mishaps [inc INTERSTELLAR]'
        self.host = ['Matt Parker']
        self.date = '2020-09-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1905, 1916, 7, 61361, 38.4, -38.4, 0.0000384, -0.0000384, 0.5) or is_close(result, 3e8) or is_error(result) or (is_real(result) and (3000 <= result <= 6357/2 or 417.45 <= result <= 1669.79))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube694(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=zUp8pkoeMss'
        self.title = 'UK Government loses data because of Excel mistake.'
        self.host = ['Matt Parker']
        self.date = '2020-10-09'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result) or result in (15841, 1048576, 16384, 65536, 1400, 47, 3597, 35175, 19.6, 0.196)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube695(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=snHKEpCv0Hk'
        self.title = 'Beautiful Trigonometry'
        self.host = ['Ben Sparks']
        self.date = '2020-06-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: any(op in formula for op in ('sin', 'cos', 'tan', 'cosec', 'sec' 'cot'))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube696(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BbnbfKbgf5Q'
        self.title = "The Incredible 'Pick Any Card' Trick Explained!"
        self.host = ['Matt Parker', 'Mark (learner of Math)']
        self.date = '2020-10-30'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (52, 36) or is_close(result, (1-1/(math.e**n) for n in range(1, 30)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube697(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9nogAYHmnNw'
        self.title = 'Spoooky maths: What is a Vampire Matrix?'
        self.host = ['Matt Parker']
        self.date = '2020-10-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'matrix'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (16, 64, 0.25, 141_345, 3141, 45, 22_962_033_171_787, 8_720_297, 2_633_171, 24_633_159_347_911, 9_354_941, 6_933_589_515_241), lambda formula, result, context: result in (3, 4, 6, 8, 33, 44, 66, 88, 23, 26, 69, 78, 2323, 2626, 6969, 7878), lambda formula, result, context: result in (15, 143, 52, 936, 7661, 135993, 49452, 883532)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube698(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=laAtv310pyk'
        self.title = 'Hat Problems'
        self.host = ['Joe Buhler']
        self.date = '2020-07-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'random'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result in (2**i - 1 for i in range(1, 20)), lambda formula, result, context: is_real(result) and result in ((1/(i + 1)) for i in range(1, 20)), lambda formula, result, context: is_real(result) and result in ((1 - 1/(i + 1)) for i in range(1, 20)), lambda formula, result, context: is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube699(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xNx3JxRhnZE'
        self.title = 'Dungeon Numbers'
        self.host = ['Neil Sloane']
        self.date = '2020-07-29'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'bases'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube700(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Rpjab--XQ0U'
        self.title = 'Squares and Tilings'
        self.host = ['Andrei Okounkov']
        self.date = '2020-08-12'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_number(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube701(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vv0bHK44Q1s'
        self.title = '569936821221962380720'
        self.host = ['Brady Haran']
        self.date = '2020-08-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (42, -80538738812075974, 80435758145817515, 12602123297335631, 3, 569936821221962380720, -569936821113563493509, -472715493453327032)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube702(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=AeqK96UX3rA'
        self.title = 'The Brussels Choice'
        self.host = ['Neil Sloane']
        self.date = '2020-08-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0 and (result % 10) not in (0, 5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube703(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-n-d1ApBTFw'
        self.title = 'Do Storks Deliver Babies?'
        self.host = ['Tim Harford']
        self.date = '2020-08-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube704(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=M0nRWcF1WJw'
        self.title = 'Predators and Prey'
        self.host = ['Tom Crawford']
        self.date = '2020-09-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result >= 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube705(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=n5bw-Y13pdY'
        self.title = "Poncelet's Porism"
        self.host = ['Daniel Litt']
        self.date = '2020-09-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube706(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=W9uVj9rf73E'
        self.title = 'Colouring Knots'
        self.host = ['Sylvain Cappell']
        self.date = '2020-10-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube707(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SUnAvL-ThMs'
        self.title = 'Bomb Blast Radius'
        self.host = ['Tom Crawford']
        self.date = '2020-10-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'unit analysis'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube708(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9p55Qgt7Ciw'
        self.title = 'The Forgotten Number System'
        self.host = ['Alex Bellos']
        self.date = '2020-11-05'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result <= 9999])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube709(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=etx0k1nLn78'
        self.title = "Why do Biden's votes not follow Benford's Law?"
        self.host = ['Matt Parker']
        self.date = '2020-11-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {39, 1655, 516, 173, 7, 20, 2042, 98.7, 0.987, 20.5}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube710(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=D1sPBCxlDQQ'
        self.title = 'How do brains count?'
        self.host = ['Brian Butterworth']
        self.date = '2020-11-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube711(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aokNwKx7gM8'
        self.title = 'Do these scatter plots reveal fraudulent vote-switching in Michigan?'
        self.host = ['Matt Parker']
        self.date = '2020-11-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {254, 452, 212, 167, 269, 183, 199, 197, 187, 217, 205, 275, 351, 170, 274, 423, 370, 124, 451, 208, 252, 327, 495, 169, 232, 183, 358, 420, 179, 287, 228, 149, 328, 294, 291, 272, 244, 370, 201, 242, 226, 292, 205, 295, 358, 342, 267, 285, 256, 187, 302, 298, 323, 308, 446, 349, 400, 371, 391, 418, 266, 364, 324, 587, 480, 302, 418, 400, 462, 307, 243, 439, 424, 390, 340, 207, 405, 200, 659, 350, 705, 595, 379, 519, 333, 596, 499, 373, 558, 564, 549, 616, 710, 574, 417, 580, 481, 398, 255, 381, 503, 448, 494, 360, 620, 556, 512, 650, 419, 328, 690, 445, 335, 658, 844, 300, 696, 588, 562, 452, 444, 541, 640, 493, 511, 678, 765, 628, 320, 598, 399, 589, 599, 422, 572, 778, 870, 287, 679, 717, 673, 666, 452, 1019, 561, 310, 671, 608, 251, 331, 440, 478, 584, 437, 403, 363, 333, 316, 364, 302, 155, 251, 554, 728, 410, 336, 292, 567, 619, 660, 678, 643, 827, 567, 534, 231, 937, 667, 546, 601, 336, 418, 283, 215, 241, 228, 229, 247, 208, 456, 374, 417, 459, 381, 458, 513, 492, 442, 314, 258, 367, 468, 234, 325, 481, 204, 256, 245, 141, 191, 164, 292, 256, 474, 342, 425, 387, 350, 340, 403, 302, 370, 487, 295, 541, 190, 518, 354, 369, 295, 583, 451, 440, 346, 380, 249, 223, 280, 550, 259, 498, 479, 509, 314, 554, 438, 287, 254, 234, 379, 326, 324, 307, 531, 365, 410, 705, 236, 266, 343, 470, 558, 646, 537, 816, 288, 304, 559, 586, 327, 202, 1006, 987, 1100, 538, 1003, 1076, 534, 840, 774, 353, 785, 760, 534, 875, 627, 703, 654, 507, 713, 502, 565, 444, 476, 347, 453, 708, 353, 397, 308, 343, 423, 612, 588, 868, 829, 261, 272, 279, 229, 185, 226, 996, 498, 667, 523, 343, 679, 983, 736, 392, 451, 260, 431, 447, 466, 460, 247, 454, 364, 243, 119, 231, 154, 139, 489, 213, 203, 277, 425, 192, 224, 342, 117, 117, 334, 51, 265, 565, 514, 41, 467, 58, 89, 213, 150, 249, 176, 199, 244, 161, 66, 301, 376, 167, 405, 281, 55, 113, 499, 320, 329, 416, 484, 382, 297, 132, 141, 125, 244, 42, 528, 284, 363, 375, 188, 346, 298, 120, 92, 91, 89, 155, 189, 50, 81, 111, 293, 48, 114, 116, 151, 149, 61, 51, 182, 541, 542, 705, 668, 669, 535, 525, 502, 396, 619, 338, 246, 232, 510, 340, 485, 398, 493, 599, 293, 468, 158, 346, 565, 197, 253, 790, 593, 341, 359, 652, 555, 486, 568, 446, 766, 707, 427, 480, 525, 949, 795, 644, 712, 530, 476, 467, 638, 637, 1008, 828, 569, 632, 688, 534, 681, 502, 681, 567, 330, 454, 491, 711, 531, 502, 532, 715, 571, 319, 197, 362, 309, 370, 277, 510, 237, 353, 247, 151, 182, 373, 270, 201, 334, 243, 258, 364, 389, 555, 287, 347, 506, 510, 274, 328, 647, 514, 765, 589, 1043, 512, 402, 682, 421, 539, 450, 344, 462, 447, 542, 852, 336, 507, 910, 636, 274, 725, 542, 624, 806, 743, 434, 579, 471, 746, 831, 424, 624, 576, 371, 761, 669, 742, 610, 579, 903, 502, 643, 591, 718, 474, 785, 910, 727, 516, 656, 652, 498, 558, 738, 656, 699, 890, 812, 886, 794, 916, 956, 564, 664, 605, 835, 787, 635, 855, 765, 808, 674, 466, 901, 933, 896, 741, 380, 884, 500, 1085, 541, 1171, 1102, 626, 1003, 668, 916, 832, 751, 819, 939, 1009, 766, 898, 934, 515, 892, 996, 766, 297, 787, 621, 790, 811, 668, 1020, 807, 1056, 1056, 729, 617, 1068, 929, 512, 1274, 1557, 584, 1216, 1075, 1056, 901, 856, 953, 1014, 975, 877, 1156, 1458, 846, 543, 1188, 694, 1134, 988, 675, 953, 1379, 1372, 540, 919, 976, 915, 919, 535, 1252, 1040, 632, 810, 954, 507, 628, 727, 698, 767, 779, 771, 698, 671, 710, 733, 609, 373, 561, 783, 1195, 676, 516, 439, 825, 929, 1125, 942, 1051, 1410, 842, 857, 393, 1311, 1284, 714, 916, 757, 841, 588, 411, 417, 420, 453, 463, 388, 998, 808, 741, 936, 820, 1059, 1142, 1125, 903, 686, 681, 755, 1159, 469, 666, 896, 362, 511, 455, 259, 365, 303, 619, 559, 800, 647, 800, 834, 697, 662, 771, 597, 781, 706, 415, 773, 292, 827, 549, 679, 407, 826, 610, 592, 480, 570, 420, 349, 465, 730, 457, 753, 732, 823, 504, 866, 773, 597, 526, 461, 761, 677, 698, 472, 886, 592, 554, 1032, 380, 446, 510, 719, 902, 1000, 857, 1214, 511, 471, 898, 937, 555, 310, 1557, 1503, 1621, 772, 1463, 1615, 829, 1311, 1124, 544, 1132, 1206, 829, 1378, 996, 1106, 1052, 789, 1153, 826, 961, 670, 765, 543, 715, 1120, 579, 534, 529, 574, 682, 956, 1073, 1363, 1294, 433, 459, 447, 368, 357, 354, 1367, 719, 945, 752, 489, 1004, 1437, 1082, 624, 674, 430, 636, 721, 714, 733, 406, 722, 553, 407, 183, 374, 253, 224, 775, 384, 322, 452, 668, 297, 376, 551, 151, 181, 502, 64, 425, 900, 833, 55, 756, 66, 154, 371, 268, 406, 255, 331, 419, 255, 131, 452, 614, 249, 705, 455, 88, 209, 789, 501, 529, 618, 749, 587, 509, 213, 234, 194, 357, 57, 735, 449, 595, 546, 291, 522, 492, 200, 133, 139, 154, 243, 299, 63, 117, 209, 476, 74, 189, 183, 268, 243, 105, 71, 302, 766, 807, 1035, 1029, 1027, 806, 855, 819, 569, 922, 518, 378, 379, 708, 507, 795, 563, 753, 905, 461, 596, 225, 524, 879, 285, 382, 1256, 964, 589, 555, 999, 904, 791, 933, 680, 1298, 1165, 710, 828, 867, 1504, 1255, 1089, 1140, 872, 827, 718, 1053, 993, 1499, 1265, 873, 1025, 1051, 779, 1031, 793, 1100, 858, 545, 734, 777, 1109, 917, 829, 876, 1027, 828, 483, 284, 516, 471, 567, 433, 782, 346, 532, 342, 233, 275, 509, 426, 317, 455, 353, 387, 582, 576, 843, 432, 566, 779, 813, 419, 476, 981, 821, 1088, 1075, 1964, 1137, 968, 1750, 820, 1010, 978, 1091, 1389, 1464, 1419, 2104, 866, 994, 1844, 1591, 840, 1054, 2139, 2190, 2466, 1556, 1930, 2237, 1329, 2095, 1983, 989, 1789, 1819, 1215, 2175, 1689, 1889, 1691, 1396, 2090, 1352, 1638, 1276, 1501, 1035, 1529, 2065, 1328, 1058, 1196, 1250, 1211, 1553, 1842, 2061, 2023, 1338, 1289, 1349, 1183, 1301, 1330, 1969, 1404, 1594, 1624, 1310, 1673, 2324, 1896, 1447, 1365, 907, 1557, 1686, 1632, 1509, 796, 1636, 1069, 1546, 746, 1573, 1381, 877, 1809, 1077, 1261, 1303, 1450, 1152, 1352, 1614, 931, 1100, 1476, 592, 1355, 1937, 1644, 359, 1565, 702, 962, 1214, 954, 1453, 1105, 1419, 1521, 1016, 759, 1552, 1577, 774, 2019, 2054, 697, 1453, 1901, 1596, 1467, 1516, 1740, 1631, 1504, 1117, 1434, 1711, 1219, 609, 1963, 1164, 1755, 1566, 981, 1499, 1907, 1598, 685, 1082, 1153, 1185, 1239, 608, 1394, 1269, 1127, 897, 1165, 716, 915, 997, 818, 849, 1101, 1581, 1552, 1746, 1771, 1803, 1441, 1251, 1405, 1375, 2173, 1222, 907, 842, 1559, 1458, 1955, 1546, 1832, 2354, 1320, 1473, 630, 1865, 2194, 1012, 1334, 2061, 1855, 1215, 990, 1446, 1356, 1260, 1421, 1087, 2334, 2011, 1496, 1802, 1731, 2606, 2427, 2266, 2075, 1590, 1536, 1502, 2253, 1478, 2225, 2215, 1260, 1559, 1530, 1051, 1421, 1127, 1754, 1447, 1374, 1410, 1608, 1983, 1651, 1512, 1683, 1665, 1647, 1214, 718, 1311, 778, 1426, 1004, 1484, 777, 1393, 973, 849, 770, 1110, 877, 681, 943, 1108, 857, 1374, 1336, 1703, 951, 1464, 1588, 1439, 965, 955, 1773, 1529, 1812, 335, 591, 300, 235, 413, 238, 340, 253, 157, 245, 242, 267, 501, 166, 233, 487, 266, 150, 274, 334, 372, 479, 248, 265, 347, 288, 388, 411, 245, 337, 348, 222, 433, 375, 451, 338, 335, 533, 301, 401, 365, 426, 269, 490, 552, 385, 249, 371, 396, 311, 256, 440, 333, 391, 444, 463, 486, 423, 525, 538, 298, 300, 281, 248, 307, 333, 437, 365, 346, 367, 223, 462, 509, 506, 401, 173, 479, 300, 426, 191, 466, 507, 247, 484, 335, 320, 333, 378, 261, 375, 460, 150, 188, 360, 98, 312, 515, 368, 42, 406, 118, 342, 317, 308, 400, 251, 544, 406, 310, 289, 378, 484, 177, 616, 713, 284, 520, 487, 494, 449, 412, 412, 374, 482, 366, 478, 693, 218, 223, 590, 295, 545, 389, 253, 381, 601, 502, 253, 240, 259, 242, 253, 83, 233, 479, 322, 139, 346, 256, 297, 287, 220, 183, 342, 368, 335, 338, 394, 369, 307, 218, 310, 229, 467, 266, 180, 147, 258, 310, 465, 264, 408, 583, 275, 323, 162, 374, 617, 168, 315, 421, 423, 305, 196, 176, 192, 224, 216, 180, 542, 434, 324, 477, 439, 601, 629, 633, 461, 372, 423, 388, 691, 235, 341, 415, 158, 255, 210, 118, 174, 139, 327, 303, 326, 305, 375, 447, 347, 322, 368, 295, 411, 219, 120, 232, 102, 309, 195, 310, 112, 243, 159, 152, 134, 190, 171, 126, 185, 180, 198, 255, 253, 314, 190, 312, 335, 310, 272, 227, 382, 351, 374, 165, 355, 227, 144, 327, 144, 180, 167, 249, 344, 354, 320, 398, 223, 167, 339, 351, 228, 108, 551, 516, 521, 234, 460, 539, 295, 471, 350, 191, 347, 446, 295, 503, 369, 403, 398, 282, 440, 324, 396, 226, 289, 196, 262, 412, 226, 137, 221, 231, 259, 344, 485, 495, 465, 172, 187, 168, 139, 172, 128, 371, 221, 278, 229, 146, 325, 454, 346, 232, 223, 170, 205, 274, 248, 273, 159, 268, 189, 164, 64, 143, 99, 85, 286, 171, 119, 175, 243, 105, 152, 209, 34, 64, 168, 13, 160, 335, 319, 14, 289, 8, 65, 158, 118, 157, 79, 132, 175, 94, 65, 151, 238, 82, 300, 174, 33, 96, 290, 181, 200, 202, 265, 205, 212, 81, 93, 69, 113, 15, 207, 165, 232, 171, 103, 176, 194, 80, 41, 48, 65, 88, 110, 13, 36, 98, 183, 26, 75, 67, 117, 94, 44, 20, 120, 225, 265, 330, 361, 358, 271, 330, 317, 173, 303, 180, 132, 147, 198, 167, 310, 165, 260, 306, 168, 128, 67, 178, 314, 88, 129, 466, 371, 248, 196, 347, 349, 305, 365, 234, 532, 458, 283, 348, 342, 555, 460, 445, 428, 342, 351, 251, 415, 356, 491, 437, 304, 393, 363, 245, 350, 291, 419, 291, 215, 280, 286, 398, 386, 327, 344, 312, 257, 164, 87, 154, 162, 197, 156, 272, 109, 179, 95, 82, 93, 136, 156, 116, 121, 110, 129, 218, 187, 288, 145, 219, 273, 303, 145, 148, 334, 307, 323, 511, 975, 558, 389, 765, 396, 540, 434, 427, 607, 605, 596, 929, 401, 405, 849, 616, 380, 385, 919, 936, 1026, 500, 754, 919, 604, 887, 777, 451, 705, 814, 526, 963, 759, 884, 758, 639, 995, 639, 824, 605, 730, 479, 772, 993, 626, 387, 599, 647, 595, 622, 949, 859, 873, 626, 665, 669, 582, 723, 679, 698, 528, 582, 482, 474, 685, 910, 753, 583, 603, 399, 683, 805, 768, 687, 337, 764, 499, 606, 262, 626, 621, 340, 789, 516, 448, 518, 634, 380, 539, 704, 175, 247, 541, 112, 477, 878, 721, 56, 703, 133, 413, 498, 437, 566, 356, 701, 588, 425, 359, 545, 747, 263, 940, 905, 332, 636, 791, 701, 677, 647, 703, 596, 701, 460, 593, 803, 325, 241, 824, 472, 793, 581, 364, 573, 818, 594, 298, 299, 336, 339, 366, 97, 271, 593, 518, 158, 429, 341, 425, 397, 266, 196, 477, 619, 629, 697, 778, 757, 594, 564, 646, 408, 790, 458, 307, 307, 462, 485, 792, 438, 677, 915, 451, 462, 232, 548, 952, 263, 460, 923, 823, 571, 406, 541, 565, 537, 587, 427, 1104, 913, 635, 848, 806, 1177, 1110, 1108, 906, 737, 796, 656, 1138, 593, 866, 886, 471, 651, 582, 366, 537, 445, 771, 618, 548, 606, 680, 872, 759, 656, 734, 637, 695, 391, 211, 381, 274, 524, 358, 589, 228, 430, 262, 244, 230, 335, 345, 246, 319, 287, 325, 486, 451, 620, 340, 535, 620, 636, 430, 387, 737, 684, 720}, lambda formula, result, context: is_close(result, (-0.40097347, -0.36253818, 0.599026525726, 0.637461818))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube712(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=HW6AzfpgpY8'
        self.title = 'Can you solve the banana puzzle?'
        self.host = ['Matt Parker', 'Hugh Hunt']
        self.date = '2020-11-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0.8])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube713(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_gCKX6VMvmU'
        self.title = '2.920050977316'
        self.host = ['James Grime']
        self.date = '2020-11-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result) or is_close(result, 2.920050977316, 1e-12)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube714(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WIibcLd_oYU'
        self.title = 'How to build a Giant Dome'
        self.host = ['Tom Crawford']
        self.date = '2020-12-04'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'cosh(' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube715(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=MZVs6wF7nC4'
        self.title = 'What was the first (known) maths mistake?'
        self.host = ['Matt Parker']
        self.date = '2020-12-09'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube716(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=OFbbiAf8kUo'
        self.title = 'Inca Knot Numbers'
        self.host = ['Alex Bellos']
        self.date = '2020-12-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube717(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ua5aOFi-DKs'
        self.title = "Why was Biden's win calculated to be ONE IN A QUADRILLION?"
        self.host = ['Matt Parker']
        self.date = '2020-12-18'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result), lambda formula, result, context: result in (1e15, 1e-15, 1_125_899_906_842_624, 1/1_125_899_906_842_624)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube718(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VFRrzzb1dvU'
        self.title = 'Butterflies and Gyroids'
        self.host = ['Sabetta Matsumoto']
        self.date = '2020-12-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and (is_close(result, 500e-9) or 450e-9 <= result <= 495e-9)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube719(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=TvlpIojusBE'
        self.title = 'I wired my tree with 500 LED lights and calculated their 3D coordinates.'
        self.host = ['Matt Parker']
        self.date = '2020-12-23'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result <= 499])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube720(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Oy-4mPro3w8'
        self.title = 'The Drag Equation (Empire State Building v Eiffel Tower)'
        self.host = ['Tom Crawford']
        self.date = '2021-01-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and is_close(result, 1e4), lambda formula, result, context: is_real(result) and (result in (9.81, 100, 2, 5, 1.225, 0.47, 0.036, 108, 58) or 1 <= result <= 1.3 or 0.5 <= result <= 1 or is_close(result, (37, 69))), lambda formula, result, context: is_real(result) and (result in (1036, 2250, 9e6, 365e6, 0.47, 0.67, 750, 28000) or 1.8 <= result <= 2 or 1.3 <= result <= 1.5 or is_close(result, (11, 12, 13)))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube721(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=fdgZQWZgEqs'
        self.title = 'Quasiperfect Numbers with Eric Lander'
        self.host = ['Eric Lander']
        self.date = '2021-01-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 1e35 and (int(result) % 2 == 1 and math.sqrt(result) % 1 == 0) and len(set(factors(result))) >= 7])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube722(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=xOXsDfMMTjs'
        self.title = 'A proof that e is irrational'
        self.host = ['Ed Copeland']
        self.date = '2021-01-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.e])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube723(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8Ko3TdPy0TU'
        self.title = 'How lucky is too lucky?: The Minecraft Speedrunning Dream Controversy Explained'
        self.host = ['Matt Parker']
        self.date = '2021-02-04'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        # slow
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result) or is_error(result), lambda formula, result, context: is_close(result, (20/423, 20/423, stats.binom.pmf(42, 262, 20/423), stats.binom.pmf(42, 262, 20/423)*100, 1-stats.binom.cdf(41, 262, 20/423), (1-stats.binom.cdf(41, 262, 20/423))*100, 1/(1-stats.binom.cdf(41, 262, 20/423))), 1e-2, 'pct'), lambda formula, result, context: is_close(result, (0.5, 50, 1-stats.binom.cdf(210, 305, 0.5), 1/(1-stats.binom.cdf(210, 305, 0.5))), 1e-2, 'pct'), lambda formula, result, context: is_close(result, ((1-stats.binom.cdf(41, 262, 20/423)) * (1-stats.binom.cdf(210, 305, 0.5)), 1/((1-stats.binom.cdf(41, 262, 20/423)) * (1-stats.binom.cdf(210, 305, 0.5)))), 1e-2, 'pct'), lambda formula, result, context: is_close(result, (8e-10, N('3.1536e19')), 1e-2, 'pct'), lambda formula, result, context: result in (20, 6, 262, 12, 42, 305, N('152.5'), 211, 42, 262)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube724(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=aQxCnmhqZko'
        self.title = 'Magic Square Party Trick'
        self.host = ['Matt Parker']
        self.date = '2016-04-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(number) and 21 <= number <= 65])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube725(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BdHFLfv-ThQ'
        self.title = 'Why π^π^π^π could be an integer (for all we know!).'
        self.host = ['Matt Parker']
        self.date = '2021-02-27'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube726(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4EIkH9EEv78'
        self.title = 'Annoying Puzzles (and Cognitive Reflection Problems)'
        self.host = ['Tim Harford']
        self.date = '2021-01-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result), lambda formula, result, context: result in (1016, 1.05)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube727(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=LVgBjRFSMYs'
        self.title = "All the World's Coronavirus fits in a Coke Can"
        self.host = ['Kit Yates']
        self.date = '2021-03-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (3_000_000, 120.6), lambda formula, result, context: is_real(result) and (1e9 <= result <= 1e11 or is_close(result, 2e17) or 80 <= result <= 120 or 80e-9 <= result <= 120e-9)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube728(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yZOi9HH5ueU'
        self.title = "Gabriel's Horn Paradox"
        self.host = ['Tom Crawford']
        self.date = '2021-02-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (math.inf, math.pi)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube729(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lmgCgzjlWO4'
        self.title = "Calculating π with Avogadro's Number"
        self.host = ['Matt Parker', 'Steve Mould']
        self.date = '2021-03-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (0.02, 400, 5e-5, 0.1, 5e-6, 0.895, 6.022e23, 282.47, 9.55e15, 8, 5.235e-22, 6.5e-19, 8e-10, 6.2e-3, 3.875), lambda formula, result, context: is_close(result, math.pi, (3.875-math.pi))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube730(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=RR3zzQP3bII'
        self.title = 'Cuneiform Numbers'
        self.host = ['Alex Bellos']
        self.date = '2021-03-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'base 60'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube731(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VTdVPNvwULM'
        self.title = 'Nightingale Diagrams'
        self.host = ['Mike Merrifield']
        self.date = '2021-03-18'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result >= 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube732(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=SMsTXQYgbiQ'
        self.title = 'Exploring the mysteries of the Prime (gaps!) Line.'
        self.host = ['Matt Parker']
        self.date = '2021-04-06'
        self.source = 'standupmaths'
        self.oeis = ['https://oeis.org/A001223', 'https://oeis.org/A002110']
        self.wiki = ['https://en.wikipedia.org/wiki/Prime_gap', 'https://en.wikipedia.org/wiki/Primorial']
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'log' in formula, lambda formula, result, context: is_prime(result), lambda formula, result, context: result == 1 or (is_int(result) and result % 2 == 0)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube733(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=s9-b-QJZdVA'
        self.title = "How did the 'impossible' Perfect Bridge Deal happen?"
        self.host = ['Matt Parker']
        self.date = '2021-04-22'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result), lambda formula, result, context: result == 2_235_197_406_895_366_368_301_559_999, lambda formula, result, context: result in (36085481721713375974666734560870400000000, 2_235_197_406_895_366_368_301_560_000, 8, 52), lambda formula, result, context: is_close(result, 4.473877774352714e-28)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube734(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=KNjPPFyEeLo'
        self.title = 'The Levine Sequence'
        self.host = ['Neil Sloane']
        self.date = '2021-03-31'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A011784'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1,2,2,3,4,7,14,42,213,2837,175450,139759600, 6837625106787,266437144916648607844, 508009471379488821444261986503540, 37745517525533091954736701257541238885239740313139682, 5347426383812697233786139576220450142250373277499130252554080838158299886992660750432)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube735(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6X2D497is6Y'
        self.title = 'Eureka Sequences'
        self.host = ['Neil Sloane']
        self.date = '2021-04-13'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A008864', 'https://oeis.org/A001043']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (3,4,6,8,12,14,18,20,24,30,32,38,42,44,48,54,60,62,68,72,74,80,84,90,98,102,104,108,110,114,128,132,138,140,150,152,158,164,168,174,180,182,192,194,198,200,212,224,228,230,234,240,242,252,258,264,270,272,278,282,284), lambda formula, result, context: result in (5,8,12,18,24,30,36,42,52,60,68,78,84,90,100,112,120,128,138,144,152,162,172,186,198,204,210,216,222,240,258,268,276,288,300,308,320,330,340,352,360,372,384,390,396,410,434,450,456,462,472,480,492,508,520)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube736(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ULhRLGzoXQ0'
        self.title = 'The Math of Being a Pig'
        self.host = ['Ben Sparks']
        self.date = '2021-04-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in range(1, 6+1), lambda formula, result, context: is_close(result, ((5/6)**n * 4 * n for n in range(1, 20))), lambda formula, result, context: is_real(result) and (0 <= result < 20 or result == 20), lambda formula, result, context: result in (65, 20, 9, 4, 1, 0.65, 0.2, 0.09, 0.04, 0.01)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube737(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=0zT16q3p24M'
        self.title = 'A Sequence with a Mistake'
        self.host = ['Neil Sloane']
        self.date = '2021-05-12'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A090805'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 2, 6, 21, 85, 430, 2586, 18109, 144880, 1303929, 13039300, 143432311, 1721187744, 22375440685, 313256169604, 4698842544075, 75181480705216, 1278085171988689, 23005533095796420, 437105128820131999, 8742102576402640000, 183584154104455440021, 4038851390298019680484)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube738(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=zTsRGQj6VT4'
        self.title = 'Gambling with the Martingale Strategy'
        self.host = ['Tom Crawford']
        self.date = '2021-05-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        # slow
        try:
            return any(
                t('', number, {'result': [number]})
                for t in [
                    lambda formula, result, context: result in (2**(k) - 1 for k in range(1, 21)) or result == 1,
                    lambda formula, result, context: result in ((1 - 1/n) for n in range(1, 10001)),
                    lambda formula, result, context: result in ((1 - 1/n)**n for n in range(1, 10001)),
                    lambda formula, result, context: is_close(result, 1/math.e)
                ]
            )
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube739(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=GAcUZ3my6E0'
        self.title = 'Parabolas and Archimedes'
        self.host = ['Johnny Ball']
        self.date = '2021-05-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_rational(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube740(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=R4OvBB9KHMA'
        self.title = 'Planing Sequences (Le Rabot)'
        self.host = ['Neil Sloane']
        self.date = '2021-06-03'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A001462', 'https://oeis.org/A319434', 'https://oeis.org/A318921', 'https://oeis.org/A027649']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 19), lambda formula, result, context: result in (2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19), lambda formula, result, context: result in (0, 0, 0, 1, 0, 0, 1, 3, 0, 0, 0, 1, 2, 1, 3, 7, 0, 0, 0, 1, 0, 0, 1, 3, 4, 2, 1, 3, 6, 3, 7, 15, 0, 0, 0, 1, 0, 0, 1, 3, 0, 0, 0, 1, 2, 1, 3, 7, 8, 4, 2, 5, 2, 1, 3, 7, 12, 6, 3, 7, 14, 7, 15, 31, 0, 0, 0, 1, 0, 0, 1, 3, 0, 0, 0, 1, 2, 1, 3, 7, 0, 0, 0, 1, 0, 0, 1, 3, 4, 2, 1, 3, 6, 3, 7, 15, 16), lambda formula, result, context: result in ((3/2)**(k-2) - 1/2 for k in range(2, 22)), lambda formula, result, context: is_int(result) and result >= 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube741(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kviwvLpnZSY'
        self.title = 'Hidden Dice Faces'
        self.host = ['Ben Sparks']
        self.date = '2021-06-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 1 <= result <= 20])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube742(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VTDKqW_GLkw'
        self.title = 'How does Dobble (Spot It) work?'
        self.host = ['Matt Parker']
        self.date = '2021-04-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = ['https://en.wikipedia.org/wiki/Fano_plane', 'https://en.wikipedia.org/wiki/Difference_set']
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (55, 57, 9, 37, 10303, 102), lambda formula, result, context: result in (0, 1, 3, 13, 32, 36, 43, 52), lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube743(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Yq3P-LhlcQo'
        self.title = 'How many 3D nets does a 4D hypercube have?'
        self.host = ['Matt Parker']
        self.date = '2021-05-14'
        self.source = 'standupmaths'
        self.oeis = 'https://oeis.org/A091159'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 11, 261, 9694, 502_110, 33_064_966, 2_642_657_228, 248_639_631_948, 26_941_775_019_280)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube744(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=yNQs_Qj46yc'
        self.title = 'Why (I thought) the Euro Ball being a Rhombicuboctahedron (would be) good for England.'
        self.host = ['Matt Parker']
        self.date = '2021-07-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1966, 2021)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube745(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=2IZh-KIAQLE'
        self.title = 'The Volume of a Sphere'
        self.host = ['Johnny Ball']
        self.date = '2021-06-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (2*math.pi, 4/3*math.pi, 2/3*math.pi))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube746(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=p3Khnx0lUDE'
        self.title = 'How do you prove a prime is infinitely fragile?'
        self.host = ['Matt Parker']
        self.date = '2021-07-28'
        self.source = 'standupmaths'
        self.oeis = 'https://oeis.org/A050249'
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (294001, 505447, 584141, 604171, 971767, 1062599, 1282529, 1524181, 2017963, 2474431, 2690201, 3085553, 3326489, 4393139, 5152507, 5564453, 5575259, 6173731, 6191371, 6236179, 6463267, 6712591, 7204777, 7469789, 7469797)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube747(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ymF1bp-qrjU'
        self.title = 'Why does this balloon have -1 holes?'
        self.host = ['Matt Parker']
        self.date = '2021-07-30'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'topology'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube748(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=8aHq_euaxPE'
        self.title = 'The most ridiculously complicated maths card trick.'
        self.host = ['Matt Parker']
        self.date = '2021-08-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'binary xor'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result <= 52])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube749(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Mf2H9WZSIyw'
        self.title = 'Why the longest English word is PAPAL and SPA is the pointiest.'
        self.host = ['Matt Parker']
        self.date = '2021-08-18'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {167, 13.1, 38.1, 57.74, 57.15, 76.79, 248.0, 77.4, 2119.5, 1548.0, 2031.8, 1229.3, 1665.5, 1090.4, 1112.9, 19.6, 655.7, 6.5, 503.3, 0.0, 19.1, 0.0, 19.1, 0.0, 19.1, 0.0, 38.1, 0.0, 43.4, 50.9, 57.7, 180.0, 57.2, 0.0, 76.8, 104.0, 1124.2, 143.3, 316.6, 0.8, 162.8, 0.9, 523.5, 310.3, 638.2, 407.0, 502.8, 294.0, 255.3, 878.2, 278.4, 798.9, 965.9, 1068.5, 989.4, 1038.4}, lambda formula, result, context: result in {19.05, 38.1, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 133.35, 152.4, 171.45, 19.64, 30.49, 46.91, 64.78, 83.17, 101.81, 120.58, 139.42, 158.31, 40.69, 50.63, 64.78, 80.96, 98.18, 115.97, 134.11, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 133.35, 152.4, 23.81, 19.64, 30.49, 46.91, 64.78, 83.17, 101.81, 120.58, 139.42, 38.4, 40.69, 50.63, 64.78, 80.96, 98.18, 115.97, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 133.35, 38.4, 23.81, 19.64, 30.49, 46.91, 64.78, 83.17, 101.81, 120.58, 44.93, 38.4, 40.69, 50.63, 64.78, 80.96, 98.18, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 55.74, 38.4, 23.81, 19.64, 30.49, 46.91, 64.78, 83.17, 101.81, 57.35, 44.93, 38.4, 40.69, 50.63, 64.78, 80.96, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 73.93, 55.74, 38.4, 23.81, 19.64, 30.49, 46.91, 64.78, 83.17, 72.7, 57.35, 44.93, 38.4, 40.69, 50.63, 64.78, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 92.47, 73.93, 55.74, 38.4, 23.81, 19.64, 30.49, 46.91, 64.78, 89.48, 72.7, 57.35, 44.93, 38.4, 40.69, 50.63, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 111.18, 92.47, 73.93, 55.74, 38.4, 23.81, 19.64, 30.49, 46.91, 107.02, 89.48, 72.7, 57.35, 44.93, 38.4, 40.69, 133.35, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 129.99, 111.18, 92.47, 73.93, 55.74, 38.4, 23.81, 19.64, 30.49, 125.01, 107.02, 89.48, 72.7, 57.35, 44.93, 38.4, 152.4, 133.35, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 148.86, 129.99, 111.18, 92.47, 73.93, 55.74, 38.4, 23.81, 19.64, 143.27, 125.01, 107.02, 89.48, 72.7, 57.35, 44.93, 171.45, 152.4, 133.35, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05, 167.77, 148.86, 129.99, 111.18, 92.47, 73.93, 55.74, 38.4, 23.81, 161.71, 143.27, 125.01, 107.02, 89.48, 72.7, 57.35, 19.64, 23.81, 38.4, 55.74, 73.93, 92.47, 111.18, 129.99, 148.86, 167.77, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 133.35, 152.4, 21.3, 34.34, 51.29, 69.34, 87.82, 106.49, 125.28, 30.49, 19.64, 23.81, 38.4, 55.74, 73.93, 92.47, 111.18, 129.99, 148.86, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 133.35, 21.3, 21.3, 34.34, 51.29, 69.34, 87.82, 106.49, 46.91, 30.49, 19.64, 23.81, 38.4, 55.74, 73.93, 92.47, 111.18, 129.99, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 34.34, 21.3, 21.3, 34.34, 51.29, 69.34, 87.82, 64.78, 46.91, 30.49, 19.64, 23.81, 38.4, 55.74, 73.93, 92.47, 111.18, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 51.29, 34.34, 21.3, 21.3, 34.34, 51.29, 69.34, 83.17, 64.78, 46.91, 30.49, 19.64, 23.81, 38.4, 55.74, 73.93, 92.47, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 69.34, 51.29, 34.34, 21.3, 21.3, 34.34, 51.29, 101.81, 83.17, 64.78, 46.91, 30.49, 19.64, 23.81, 38.4, 55.74, 73.93, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 87.82, 69.34, 51.29, 34.34, 21.3, 21.3, 34.34, 120.58, 101.81, 83.17, 64.78, 46.91, 30.49, 19.64, 23.81, 38.4, 55.74, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 106.49, 87.82, 69.34, 51.29, 34.34, 21.3, 21.3, 139.42, 120.58, 101.81, 83.17, 64.78, 46.91, 30.49, 19.64, 23.81, 38.4, 133.35, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 125.28, 106.49, 87.82, 69.34, 51.29, 34.34, 21.3, 158.31, 139.42, 120.58, 101.81, 83.17, 64.78, 46.91, 30.49, 19.64, 23.81, 152.4, 133.35, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05, 144.14, 125.28, 106.49, 87.82, 69.34, 51.29, 34.34, 40.69, 38.4, 44.93, 57.35, 72.7, 89.48, 107.02, 125.01, 143.27, 161.71, 21.3, 21.3, 34.34, 51.29, 69.34, 87.82, 106.49, 125.28, 144.14, 19.05, 38.1, 57.15, 76.2, 95.25, 114.3, 50.63, 40.69, 38.4, 44.93, 57.35, 72.7, 89.48, 107.02, 125.01, 143.27, 34.34, 21.3, 21.3, 34.34, 51.29, 69.34, 87.82, 106.49, 125.28, 19.05, 19.05, 38.1, 57.15, 76.2, 95.25, 64.78, 50.63, 40.69, 38.4, 44.93, 57.35, 72.7, 89.48, 107.02, 125.01, 51.29, 34.34, 21.3, 21.3, 34.34, 51.29, 69.34, 87.82, 106.49, 38.1, 19.05, 19.05, 38.1, 57.15, 76.2, 80.96, 64.78, 50.63, 40.69, 38.4, 44.93, 57.35, 72.7, 89.48, 107.02, 69.34, 51.29, 34.34, 21.3, 21.3, 34.34, 51.29, 69.34, 87.82, 57.15, 38.1, 19.05, 19.05, 38.1, 57.15, 98.18, 80.96, 64.78, 50.63, 40.69, 38.4, 44.93, 57.35, 72.7, 89.48, 87.82, 69.34, 51.29, 34.34, 21.3, 21.3, 34.34, 51.29, 69.34, 76.2, 57.15, 38.1, 19.05, 19.05, 38.1, 115.97, 98.18, 80.96, 64.78, 50.63, 40.69, 38.4, 44.93, 57.35, 72.7, 106.49, 87.82, 69.34, 51.29, 34.34, 21.3, 21.3, 34.34, 51.29, 95.25, 76.2, 57.15, 38.1, 19.05, 19.05, 134.11, 115.97, 98.18, 80.96, 64.78, 50.63, 40.69, 38.4, 44.93, 57.35, 125.28, 106.49, 87.82, 69.34, 51.29, 34.34, 21.3, 21.3, 34.34, 114.3, 95.25, 76.2, 57.15, 38.1, 19.05}, lambda formula, result, context: result in {0.0, 1.13, 2.46, 3.87, 4.15, 2.62, 6.52, 7.35, 8.43, 9.87, 6.86, 11.89, 10.72, 13.63, 14.93, 15.42, 14.7, 17.74, 17.1, 19.98, 20.85, 21.56, 13.24, 23.96, 23.31, 25.2, 25.42, 27.88, 26.73, 29.74, 29.19, 31.61, 32.59, 29.57, 30.89, 35.04, 31.75, 37.3, 38.66, 38.9, 40.6, 41.63, 42.78, 41.54, 44.47, 36.03, 46.93, 9.25, 47.12, 48.31, 50.91, 50.79, 52.0, 53.13, 52.56, 46.61, 48.81, 57.99, 57.65, 58.86, 52.94, 61.1, 62.72, 63.43, 61.88, 65.18, 66.87, 67.75, 68.11, 69.05, 68.92, 71.29, 72.53, 73.19, 74.29, 74.22, 76.68, 76.87, 78.95, 77.95, 80.54, 80.62, 82.87, 16.5, 84.05, 85.35, 17.22, 87.4, 88.21, 89.1, 89.7, 88.75, 92.15, 92.81, 94.17, 95.61, 96.68, 97.52, 95.13, 96.93, 94.61, 98.03, 102.09, 102.91, 104.04, 105.98, 100.25, 101.81, 102.34, 109.77, 110.56, 111.6, 112.78, 113.44, 113.63, 114.34, 116.57, 116.09, 117.78, 119.98, 120.32, 121.36, 119.02, 119.96, 120.88, 125.66, 125.84, 126.29, 126.41, 127.35, 129.45, 129.81, 131.19, 131.47, 132.91, 133.99, 133.15, 136.05, 137.73, 133.67, 137.01, 140.53, 141.34, 141.11, 143.97, 144.15, 142.91, 146.17, 147.61, 147.97, 146.78, 149.23, 151.93, 151.65, 153.87, 151.01, 155.22, 156.04, 157.17, 157.29, 153.03, 160.82, 154.87, 162.9, 163.14, 163.41, 159.55, 166.76, 167.47, 168.57, 169.22, 170.91, 170.27, 172.15, 171.98, 171.44, 175.03, 175.3, 177.84, 178.84, 180.0, 10.19, 35.75, 36.19, 176.05, 178.18, 178.99, 11.22, 7.0, 38.03, 13.19, 25.72, 39.91, 39.94, 39.72, 39.5, 40.25, 8.75, 41.78, 43.56, 5.44, 43.06, 5.94, 45.78, 45.69, 45.47, 7.94, 7.44, 46.25, 9.0, 47.69, 47.41, 49.25, 49.81, 10.75, 51.19, 52.34, 53.5, 54.69, 8.97, 4.91, 55.84, 11.5, 56.78, 6.91, 6.41, 0.52, 58.47, 58.66, 7.41, 8.41, 12.0, 61.59, 62.53, 10.97, 65.66, 65.13, 13.5, 15.66, 66.93, 2.63, 16.19, 67.94, 4.88, 17.19, 17.66, 18.16, 69.44, 69.25, 18.38, 6.38, 19.44, 70.35, 19.88, 7.88, 20.38, 20.63, 21.16, 72.35, 72.57, 72.43, 22.19, 22.16, 73.16, 74.93, 74.13, 24.88, 75.28, 75.32, 24.94, 25.69, 26.94, 27.41, 78.37, 78.06, 78.84, 29.63, 80.81, 4.35, 30.88, 81.18, 83.56, 83.35, 7.85, 83.88, 83.18, 84.6, 8.35, 86.82, 86.34, 88.32, 88.38, 12.13, 12.63, 88.03, 90.84, 90.57, 91.91, 93.93, 93.18, 95.62, 97.5, 97.13, 98.82, 100.06, 100.69, 100.62, 101.44, 1.8, 102.94, 1.3, 104.68, 104.9, 105.5, 106.06, 5.07, 107.69, 107.82, 6.32, 108.97, 109.38, 109.65, 8.07, 110.28, 9.32, 111.22, 112.37, 112.62, 11.57, 12.79, 114.4, 115.53, 23.5, 14.32, 116.25, 15.54, 3.04, 16.6, 118.66, 16.85, 16.1, 4.54, 16.82, 119.19, 17.85, 17.29, 122.44, 122.18, 1.15, 21.32, 123.12, 123.6, 22.79, 124.43, 125.56, 125.13, 24.85, 126.87, 126.59, 126.43, 25.04, 127.13, 25.85, 26.1, 128.03, 128.45, 128.57, 128.06, 129.21, 2.51, 129.62, 28.07, 28.32, 130.13, 130.89, 129.04, 29.1, 130.36, 131.97, 131.44, 131.07, 30.29, 131.5, 132.45, 131.94, 131.29, 133.0, 6.01, 133.78, 32.79, 32.51, 7.76, 134.46, 135.98, 135.36, 8.01, 135.62, 34.04, 136.55, 9.76, 9.26, 135.86, 136.01, 137.17, 137.34, 137.56, 136.4, 36.29, 138.37, 36.73, 138.85, 138.09, 137.7, 139.47, 139.4, 139.02, 38.51, 38.23, 13.26, 140.45, 28.25, 38.01, 141.16, 14.51, 141.22, 135.18, 40.07, 142.4, 142.82, 142.27, 142.25, 41.04, 143.2, 42.57, 43.26, 145.67, 44.26, 146.31, 45.76, 147.89, 45.48, 3.76, 3.26, 46.04, 148.67, 148.39, 148.11, 48.01, 150.93, 150.26, 48.13, 49.57, 151.83, 151.53, 50.26, 0.6, 154.28, 154.8, 154.74, 6.5, 156.18, 157.09, 5.73, 158.2, 159.15, 159.0, 58.57, 7.23, 160.56, 160.02, 161.24, 60.35, 162.78, 162.26, 61.07, 164.58, 164.05, 165.07, 166.29, 166.2, 14.23, 14.98, 15.45, 15.95, 168.11, 168.06, 16.45, 169.7, 17.98, 170.13, 170.09, 170.32, 18.73, 5.2, 171.57, 18.98, 6.2, 19.48, 171.25, 172.06, 172.55, 7.95, 172.65, 1.56, 173.13, 7.2, 2.81, 175.96, 175.94, 23.23, 24.01, 24.7, 177.6, 24.26, 25.98, 26.7, 27.01, 2.67, 130.84, 28.73, 28.01, 3.42, 30.23, 5.92, 8.17, 3.78, 3.53, 12.67, 15.92, 5.39, 5.64, 6.89, 0.94, 1.69, 2.93, 3.86, 2.18, 3.23, 3.98, 3.65, 0.56, 2.02, 3.4, 3.35, 3.11, 19.53, 8.89, 8.39, 10.86, 10.39, 20.78, 12.11, 13.86, 135.15, 16.11, 16.36, 4.86, 17.86, 17.61, 17.17, 4.11, 5.86, 18.61, 18.92, 6.36, 19.83, 19.33, 19.08, 7.11, 20.08, 20.17, 2.22, 22.86, 22.83, 22.39, 23.39, 23.89, 24.42, 26.39, 27.83, 2.08, 28.17, 29.64, 31.33, 31.83, 31.67, 6.33, 32.89, 7.58, 7.83, 1.44, 33.42, 33.05, 8.33, 35.36, 35.11, 35.39, 11.33, 37.14, 38.2, 14.33, 14.83, 40.05, 15.83, 42.05, 42.58, 5.3, 5.05, 44.7, 45.58, 46.11, 27.28, 47.64, 47.89, 50.64, 51.55, 53.67, 54.61, 56.92, 56.2, 6.27, 57.67, 59.14, 60.7, 9.27, 10.3, 10.55, 30.78, 10.27, 62.89, 12.05, 12.27, 15.27, 16.77, 67.45, 17.05, 17.77, 18.27, 69.08, 69.95, 19.52, 70.79, 19.05, 70.99, 20.74, 71.86, 21.99, 21.8, 21.3, 21.74, 21.52, 32.28, 73.3, 73.01, 23.8, 23.55, 23.3, 74.45, 24.3, 75.96, 25.77, 25.24, 2.24, 80.02, 5.24, 31.77, 34.28, 83.42, 1.1, 84.96, 84.71, 8.49, 85.98, 86.27, 86.29, 10.99, 88.49, 88.61, 89.55, 89.27, 13.74, 91.36, 2.71, 3.46, 93.73, 94.76, 95.71, 7.46, 97.39, 97.77, 2.32, 98.8, 98.67, 3.32, 98.04, 99.58, 99.17, 99.71, 100.2, 101.14, 0.95, 1.24, 102.83, 102.96, 1.03, 1.07, 1.91, 1.86, 0.49, 1.74, 4.93, 106.26, 5.43, 6.68, 108.76, 109.48, 109.73, 110.29, 110.33, 111.7, 111.2, 10.43, 35.57, 112.92, 113.26, 12.43, 114.7, 114.23, 13.18, 115.24, 115.76, 13.46, 14.21, 116.14, 16.68, 118.24, 118.77, 16.43, 119.3, 18.68, 120.49, 19.4, 19.18, 121.86, 121.11, 121.26, 20.96, 122.17, 122.01, 122.42, 21.65, 123.48, 123.92, 123.99, 124.99, 124.51, 23.68, 125.46, 23.18, 126.23, 126.73, 127.42, 127.58, 26.21, 27.68, 27.46, 27.15, 27.93, 28.71, 29.65, 29.15, 31.71, 6.65, 32.87, 32.71, 33.15, 33.21, 8.87, 8.9, 8.65, 34.27, 35.93, 10.12, 10.15, 36.49, 11.62, 37.71, 38.49, 33.69, 14.87, 14.62, 14.9, 40.21, 40.96, 15.12, 41.37, 41.24, 41.9, 42.27, 42.12, 4.12, 5.62, 5.37, 5.12, 44.37, 47.49, 48.62, 48.96, 49.18, 50.4, 0.83, 51.27, 0.87, 2.34, 57.43, 7.59, 8.09, 59.46, 9.09, 60.46, 9.59, 10.59, 10.09, 62.02, 62.4, 12.84, 14.09, 15.34, 16.12, 4.06, 17.84, 4.56, 5.56, 20.84, 20.06, 21.62, 21.09, 24.37, 25.81, 25.09, 5.22, 5.72, 29.12, 30.81, 31.56, 19.72, 32.31, 9.81, 9.78, 10.78, 10.03, 11.56, 20.22, 12.53, 12.06, 13.31, 13.06, 14.81, 4.78, 6.03, 2.89, 22.47}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube750(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=gjtTcyWL0NA'
        self.title = 'What is the area of a Squircle?'
        self.host = ['Matt Parker']
        self.date = '2021-09-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 4 or result == 1.5 or is_close((1.198140234, 3.70814935460274983), result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube751(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=g3R_tc7YrFI'
        self.title = 'Solving the mystery of the impossible cord.'
        self.host = ['Matt Parker', 'Susan Okereke', 'Steve Mould']
        self.date = '2021-09-17'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube752(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=QFj-hF8XDQ0'
        self.title = 'Why Do Bees Make Rhombic Dodecahedrons?'
        self.host = ['Matt Parker', 'Maddie Moate']
        self.date = '2021-10-06'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 120) or is_close(result, (math.sqrt(2), math.sqrt(3), math.sqrt(5)/4, math.sqrt(2)/2, math.sqrt(3)/2, 109.5))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube753(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ckcdqlo3pYc'
        self.title = 'Measure the Earth’s Radius! (with this one complicated trick)'
        self.host = ['Matt Parker', 'Hannah Fry']
        self.date = '2021-10-07'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and (is_close(result, (22.9, 20, 100, 200), 1e-2) or 1 <= result <= 2 or 263.1 <= result <= 309 or 875 <= result <= 6371)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube754(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=ueEOHk1UzrA'
        self.title = 'Find your own ABC Conjecture Triple'
        self.host = ['Matt Parker']
        self.date = '2021-10-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Abc_conjecture'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube755(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-tGusgPTSm4'
        self.title = 'The Deepest Maths Video Ever [pressure vs depth]'
        self.host = ['Matt Parker', 'Richard Garriott de Cayeux']
        self.date = '2021-10-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (10900, 11, 6.8, 54.2, 1.96, 1.07474785)) or result in (112494873, 112494.873, 10897, 10925, 10935)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube756(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=gPIRLQZnRNk'
        self.title = 'Can you make a hole in a thing bigger than the thing?'
        self.host = ['Matt Parker']
        self.date = '2021-10-31'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 3/4 * math.sqrt(2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube757(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=31Om4VrSzb8'
        self.title = 'The bubble that breaks maths.'
        self.host = ['Matt Parker']
        self.date = '2021-11-05'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and (1.016 <= result <= 1.12 or 1.016/2 <= result <= 1.12/2 or result in (0.5, 0.4, 0.25) or is_close(result, (0.4651908, 1.6104887, 0.0688092, 0.9303816, 0.84623, 52.77, 0.5277, 66.274, 0.66274, 0.71))), lambda formula, result, context: 'cosh' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube758(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=27qhUZbHKao'
        self.title = 'Three Dice Trick'
        self.host = ['Ben Sparks']
        self.date = '2021-07-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 7])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube759(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6z4qRhpBIyA'
        self.title = 'Chaotic Balls (and other animations)'
        self.host = ['Matt Henderson']
        self.date = '2021-07-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube760(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=VZ25tZ9z6uI'
        self.title = 'A Problem with Rectangles'
        self.host = ['Tom Crawford']
        self.date = '2021-07-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 2 and result not in (3, 4)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube761(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BdEWCxt8C0M'
        self.title = 'Mathematics is all about SHORTCUTS'
        self.host = ['Marcus du Sautoy']
        self.date = '2021-08-08'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: not is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube762(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=cE44nr4d3iY'
        self.title = 'Get Off The Earth (a famous & bamboozling problem)'
        self.host = ['Ben Sparks']
        self.date = '2021-08-19'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 12 or result == 13])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube763(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=GVhFBujPlVo'
        self.title = 'Why it’s mathematically impossible to share fair'
        self.host = ['Matt Parker']
        self.date = '2021-11-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Apportionment_paradox'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (27770.5, 28364.4, 28475, 29460.17, 29462.14, 29605, 29707.94, 29928.34, 30026.62, 30144.55, 30919.86, 30946, 34223, 34352.5, 35421, 125401, 275209, 70945, 281127, 54844, 147102, 513624, 123781, 298335, 364391, 523287, 62322, 62493, 244161, 274552, 1368777, 556822, 581434, 1049314, 83040, 389596, 390770, 235764, 895305, 3.14, 6.88, 1.77, 7.03, 1.37, 3.68, 12.84, 3.09, 7.46, 9.11, 13.08, 1.56, 6.1, 6.86, 34.22, 13.92, 14.54, 26.23, 2.08, 9.74, 9.77, 5.89, 22.38, 3, 6, 1, 7, 12, 9, 13, 34, 14, 26, 2, 5), lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube764(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=akZ8JJ4gGLs'
        self.title = 'The Lightning Algorithm'
        self.host = ['Matt Henderson']
        self.date = '2021-08-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Breadth-first_search'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result >= 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube765(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BO2yMdU0Rq4'
        self.title = 'Area of the Q'
        self.host = ['Johnny Ball']
        self.date = '2021-09-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube766(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vU-g6mC1F0g'
        self.title = "The Strange Orbit of Earth's Second Moon (plus The Planets)"
        self.host = ['Matt Henderson']
        self.date = '2021-09-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (8, 13, 5, 1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube767(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sGkwG8c0__E'
        self.title = 'Stacked Dice Trick'
        self.host = ['Ben Sparks']
        self.date = '2021-09-22'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (1 <= result <= 6 or result == 7 or 15 <= result <= 20)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube768(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FCczHiXPVcA'
        self.title = 'Finite Fields & Return of The Parker Square'
        self.host = ['Matt Parker']
        self.date = '2021-10-07'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result) or (is_int(result) and len(set(factors(result, FACTORS_PRIME))) == 1), lambda formula, result, context: result in (0, 1, 9, 9*9, 11, 11*11, 6, 6*6, 14, 14*14, 8, 8*8, 12, 12*12, 16, 16*16) or result in (v%29 for v in (0, 1, 9, 9*9, 11, 11*11, 6, 6*6, 14, 14*14, 8, 8*8, 12, 12*12, 16, 16*16)), lambda formula, result, context: result in (29, 0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 43, 47, 67)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube769(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=pG8KorwT_Pg'
        self.title = 'Trapped Water and Tiny Holes'
        self.host = ['Tom Crawford']
        self.date = '2021-10-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 0 < result < 1.7])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube770(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sToqbqP0tFk'
        self.title = 'Music on a Clear Möbius Strip'
        self.host = ['Marcus Du Sautoy']
        self.date = '2021-10-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 14])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube771(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PGuRmqpr6Oo'
        self.title = 'Key to the Tower of Hanoi'
        self.host = ['Ayliean MacDonald']
        self.date = '2021-10-27'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (2**n - 1 for n in range(1, 200))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube772(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=z2x3SSBVGJU'
        self.title = 'The Doomsday Algorithm'
        self.host = ['James Grime']
        self.date = '2021-10-31'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Doomsday_rule'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (4, 6, 8, 10, 12, 5, 9, 7, 11, 3, 4, 28, 29, 14, 2000)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube773(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=KZ1BVlURwfI'
        self.title = 'A Video about the Number 10'
        self.host = ['James Grime']
        self.date = '2021-11-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Friendly_number'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 10])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube774(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=hSsRcpIsunk'
        self.title = 'Infinitely Many Touching Circles'
        self.host = ['Matt Henderson']
        self.date = '2021-11-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'sin' in formula or 'cos' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube775(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NFLb1IPlY_k'
        self.title = 'How to make railway timetables (with graphs)'
        self.host = ['Hannah Fry']
        self.date = '2021-11-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 0 <= result < 24])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube776(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=_MscGSN5J6o'
        self.title = 'Witness Numbers (and the truthful 1,662,803)'
        self.host = ['Matt Parker']
        self.date = '2021-11-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result), lambda formula, result, context: is_real(result) and result < 0 and is_int(math.log(result, 4)), lambda formula, result, context: result in (-1, 1), lambda formula, result, context: result in (2, 3, 1_373_653, 5, 25_326_001, 31, 73, 9_080_191, 13, 23, 1_662_803, 1_122_004_669_633, 7, 11, 2_152_302_898_747, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 318_665_857_834_031_151_167_461)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube777(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=4K-Jx914NcQ'
        self.title = 'Is there an equation for a triangle?'
        self.host = ['Matt Parker']
        self.date = '2021-12-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'abs(' in formula or 'sign(' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube778(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=JbfhzlMk2eY'
        self.title = 'Hitomezashi Stitch Patterns'
        self.host = ['Ayliean MacDonald']
        self.date = '2021-12-06'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'boolean'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_random(formula, result) or result in (0, 1)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube779(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dGnIJFzkLI4'
        self.title = 'What is the factorial of -½?'
        self.host = ['Matt Parker']
        self.date = '2021-12-10'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = 'complex factorial'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'factorial' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube780(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=JXtfKMH6X44'
        self.title = 'Omicron (the symbol) in Mathematics'
        self.host = ['Tony Padilla']
        self.date = '2021-12-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 70])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube781(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vKlVNFOHJ9I'
        self.title = 'The Most Wanted Prime Number'
        self.host = ['Neil Sloane']
        self.date = '2021-12-15'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'There might be some extra tests to include here'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (10, 2446) or result == 12345678910987654321, lambda formula, result, context: is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube782(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=1kYGbMK1oA4'
        self.title = 'The Largest Small Hexagon'
        self.host = ['James Grime']
        self.date = '2021-12-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (112.8, 102.5, 116.3, 159.6), 1e-1) or is_close(result, (0.641, 0.558, 0.349), 1e-3) or result == 1])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube783(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=mZBwsm6B280'
        self.title = "Bertrand's Paradox (with 3blue1brown)"
        self.host = ['Grant Sanderson']
        self.date = '2021-12-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (math.sqrt(3), 1/3)) or result in (0.25, 0.5), lambda formula, result, context: is_random(formula, result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube784(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=m0LVEvtjK4M'
        self.title = 'Conic Loaf of Bread'
        self.host = ['Cliff Stoll']
        self.date = '2021-12-25'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube785(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wG2QEDm-k4U'
        self.title = 'Why does the occasional solar eclipse go backwards?'
        self.host = ['Matt Parker']
        self.date = '2021-12-24'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 22.1 <= result <= 24.5])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube786(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=m4Uth-EaTZ8'
        self.title = 'Stones on an Infinite Chessboard'
        self.host = ['Neil Sloane']
        self.date = '2022-01-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'interesting programming problem'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 16, 28, 38, 49, 60)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube787(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=NHZt8eBKcRA'
        self.title = 'What is a Number?'
        self.host = ['Asaf Karagila']
        self.date = '2022-01-14'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_number(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube788(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=WuMRJf6B5Q4'
        self.title = 'My 500-LED xmas tree got into Harvard'
        self.host = ['Matt Parker']
        self.date = '2021-12-25'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result) or result == 0.75])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube789(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/shorts/i9CdGc3e7-g'
        self.title = 'The Parker Square'
        self.host = []
        self.date = '2022-01-20'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (29, 1, 47, 41, 37, 23)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube790(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kwrDX5qkwvA'
        self.title = 'Tunnelling through a Mountain'
        self.host = ['Hannah Fry']
        self.date = '2022-01-23'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and result > 0])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube791(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=kMBj2fp52tA'
        self.title = 'The Plotting of Beautiful Curves (Euler Spirals and Sierpiński Triangles)'
        self.host = ['Matt Henderson']
        self.date = '2022-02-01'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 0 <= result <= 360, lambda formula, result, context: result in (0.0483394,)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube792(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=tkC1HHuuk7c'
        self.title = 'Plotting Pi and Searching for Mona Lisa'
        self.host = ['Matt Henderson']
        self.date = '2022-02-02'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, math.pi), lambda formula, result, context: is_int(result) and 0 <= result <= 9])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube793(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=DK3njNP-Qz0'
        self.title = 'The Mathematics of Surviving Zombies'
        self.host = ['Thomas Woolley']
        self.date = '2022-02-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube794(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=-IjGexS1T8U'
        self.title = 'The Tetrahedral Boat'
        self.host = ['Marcus du Sautoy']
        self.date = '2022-02-26'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (1, 2, 3, 4, 5)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube795(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=q8Umr0BLMiU'
        self.title = 'The Coca-Cola Klein Bottle'
        self.host = ['Cliff Stoll']
        self.date = '2022-03-09'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube796(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=DmfxIhmGPP4'
        self.title = 'The Reciprocals of Primes'
        self.host = ['Matt Parker']
        self.date = '2022-03-14'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A002371'
        self.wiki = 'https://en.wikipedia.org/wiki/Reciprocals_of_primes'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube797(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=6ofIBoWGc7k'
        self.title = 'Big Factorials'
        self.host = ['Ken McLaughlin']
        self.date = '2022-03-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: '!' in formula])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube798(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=n4gmYjyI3vo'
        self.title = 'Twin Proofs for Twin Primes'
        self.host = ['Ben Sparks']
        self.date = '2022-03-27'
        self.source = 'Numberphile'
        self.oeis = ['https://oeis.org/A077800']
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube799(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=wYDh5d9pfu8'
        self.title = 'How do fish swim so quickly?'
        self.host = ['Tadashi Tokieda']
        self.date = '2022-03-30'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/K%C3%A1rm%C3%A1n_vortex_street'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: False])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube800(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=3cNdM7W0VlQ'
        self.title = 'The Problem With Infinite Summations On YouTube'
        self.host = ['Matt Parker']
        self.date = '2022-02-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube801(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=BstloCx8KDk'
        self.title = "The Coupon Collector's Problem (with Geoff Marshall)"
        self.host = ['Matt Parker', 'Geoff Marshall']
        self.date = '2022-02-12'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Coupon_collector%27s_problem'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and 0 <= result <= 59, lambda formula, result, context: result == 281])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube802(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=Ffa8-S_71xo'
        self.title = 'Twos-Day Tuesday! 22 YouTubers celebrate all things "two" and nothing goes wrong.'
        self.host = ['Matt Parker', 'James Grime', 'Katie Steckles', 'Steve Mould', 'Ayliean MacDonald', 'Ben Sparks', 'Grant Sanderson', 'Hannah Fry', 'Simone Giertz', 'Mehdi Sadaghdar', 'Mithuna Yoganathan', 'Geoff Marshall', "Jade 'Up and Atom'", 'Jeremy Fielding', 'Eddie Woo', 'Vi Hart', 'Rohin Francis', 'Tom Crawford', 'Destin Sandlin', 'Tom Scott']
        self.date = '2022-02-22'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(
                t('', number, {'result': [number]})
                for t in [
                    lambda formula, result, context: is_int(result) and result > 1 and is_int(math.log2(result)),
                    lambda formula, result, context: result in {256, 7, 127, 2_147_483_647, 2**127 - 1, 3, 2, 5, 6, math.inf, 0.02, 222, 222002, 22},
                    lambda formula, result, context: is_real(result) and 0 < result <= 1 and is_int(math.log2(result))
                ]
            )
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube803(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=vXWvptwoCl8'
        self.title = "Why don't Jigsaw Puzzles have the correct number of pieces?"
        self.host = ['Matt Parker']
        self.date = '2022-03-03'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (200, 204, 150, 33, 22.8, 1000, 11, 14, 500, 530, 530, 1000, 1, 70, 50, 1008, 80, 60, 1530, 98, 68.6, 2000, 98, 37.5, 1000), lambda formula, result, context: is_close(result, (1.3611, 1.417, 1.5, 1.04, 1.102, 1.4474, 1.6, 1.1055, 1.2727, 1.25, 1.0102, 1.6, 1.4, 1.2857, 1.0009, 80/60, 45/34, 1.007, 98/68.6, 50/40, 1.1429, 98/37.5, 50/20, 1.0453)), lambda formula, result, context: is_error(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube804(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dtiLxLrzjOQ'
        self.title = 'Can we calculate 100 digits of π by hand? The William Shanks method.'
        self.host = ['Matt Parker', 'Keith Moore', 'Sophie Maclean', 'Matthew Scroggs', 'Hazel Minty', 'Christian Lawson-Perfect', 'Sophie Bleau']
        self.date = '2022-03-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_close(result, (16*math.atan(1/5), 4*math.atan(1/239))), lambda formula, result, context: is_real(result) and 3.14159265358868298 <= result <= math.pi])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube805(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=sseSi0k3Ecg'
        self.title = 'What was the most expensive book ever?'
        self.host = ['Matt Parker']
        self.date = '2022-04-08'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and 1_730_045.91 <= result < 1.270589 * 20_000_000, lambda formula, result, context: is_close(result, (1.270589, 0.9983, 1.26843)), lambda formula, result, context: is_close(result, (2_000_000_000, 56_000_000_000, 4_100_000_000))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube806(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=jMxoGqsmk5Y'
        self.title = 'How Roman numerals broke the official dog database.'
        self.host = ['Matt Parker', 'Skylab']
        self.date = '2022-04-14'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_int(result) and (0 < result <= 37 or 39 <= result <= 77 or 89 <= result <= 127), lambda formula, result, context: result in (3_999, 1_308, 4_000, 6_000, 1_347, 133), lambda formula, result, context: result == 39**50 * 37])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube807(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=dET2l8l3upU'
        self.title = 'I found Amongi in the digits of pi!'
        self.host = ['Matt Parker']
        self.date = '2022-04-29'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.pi or result in (143352, 1227692, 2477785, 53_559, 163_922, 2_054, 1_424_490, 521_165) or is_prime(result)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube808(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=nMqdRu9gGGs'
        self.title = 'New World Record! 100 Trillion digits of π.'
        self.host = ['Matt Parker', 'Emma Haruka Iwao']
        self.date = '2022-06-15'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = 'https://en.wikipedia.org/wiki/Chudnovsky_algorithm'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == math.pi or result in (100_000_000_000_000, 43_420_162_171_515, 14, 17_475_119_650_043, 23_876_384_085_914, 26_798_580_282_639, 30_538_916_340_408, 34_165_554_003_935, 56_826_305_253_341, 61_939_972_123_252, 63_634_253_668_531, 88_851_388_178_278, 31415926535897, 3141592653589)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube809(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=PDLQadz1KCc'
        self.title = 'What is wrong with this sine memorisation pattern?'
        self.host = ['Matt Parker']
        self.date = '2022-06-20'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: 'sin(' in formula or result in (0, 1/2, math.sqrt(2)/2, math.sqrt(3)/2, 1, 30, 45, 60, 90, math.pi/6, math.pi/4, math.pi/3, math.pi/2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube810(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=X_DdGRjtwAo'
        self.title = 'The unexpected logic behind rolling multiple dice and picking the highest.'
        self.host = ['Matt Parker']
        self.date = '2022-07-01'
        self.source = 'standupmaths'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (4, 6, 12, 20, 60, 120), lambda formula, result, context: any(result in ((2*i+1)/(d*d) for i in range(d)) for d in (4, 6, 12, 20, 60, 120)), lambda formula, result, context: any(result in (100*(2*i+1)/(d*d) for i in range(d)) for d in (4, 6, 12, 20, 60, 120)), lambda formula, result, context: result in ((d+1)*(4*d-1)/(6*d) for d in (4, 6, 12, 20, 60, 120)), lambda formula, result, context: result in (2/3, 3/4), lambda formula, result, context: result in ((n+1)*(3*n-1)/(4*n) for n in (4, 6, 12, 20, 60, 120))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube811(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CoJtruAGfTY'
        self.title = 'Drawing an Egg (with a Pentagon)'
        self.host = ['Johnny Ball']
        self.date = '2022-04-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result==5])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube812(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=CRj-sbi2i2I'
        self.title = "Euler's Formula"
        self.host = ['Tom Crawford']
        self.date = '2022-04-24'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_complex(result), lambda formula, result, context: result in (math.e, math.pi, 1j, 1, -1, 0)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube813(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=9RvqE1CQXfI'
        self.title = 'How to write 100,000,000,000,000 poems'
        self.host = ['Marcus du Sautoy']
        self.date = '2022-05-03'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'Could do n+7 poetry generator'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in (14, 100_000_000_000_000), lambda formula, result, context: result == 7])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube814(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=FkVe8qrT0LA'
        self.title = 'Two Candles, One Cake'
        self.host = ['Ben Sparks']
        self.date = '2022-05-10'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 2, 1/3}])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube815(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=l5gUrDg01cQ'
        self.title = 'Two Candles, One Cake (Part 2)'
        self.host = ['Ben Sparks']
        self.date = '2022-05-11'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result in {1, 2}, lambda formula, result, context: is_close(result, (0.16, 0.19, 0.3, 0.325), 1e-2)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube816(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=KdZrxkix9Mk'
        self.title = 'A number NOBODY has thought of'
        self.host = ['Tony Padilla']
        self.date = '2022-05-17'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = "some similarities to Sloane's gap"
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_real(result) and result > 1.76e67])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube817(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=p-HN_ICaCyM'
        self.title = 'The Troublemaker Number'
        self.host = ['Harini Desiraju']
        self.date = '2022-05-23'
        self.source = 'Numberphile'
        self.oeis = 'https://oeis.org/A030127'
        self.wiki = 'https://en.wikipedia.org/wiki/Somos_sequence'
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 420514/7 or result == 8, lambda formula, result, context: result in (17, 19, 20, 22, 24, 27, 28, 30, 33, 34, 36, 39, 41, 42, 44, 46, 48, 51, 52, 55, 56, 58, 60, 62, 65, 66, 68, 70, 72, 75, 76, 78, 81, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 107, 108, 110, 112, 114, 116, 118, 120, 123, 124, 126, 129, 130, 132, 134, 136, 138)])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube818(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=33YSWaR3kAQ'
        self.title = 'Primes and Primitive Sets (an Erdős Conjecture is cracked)'
        self.host = ['Jared Duker Lichtman']
        self.date = '2022-06-16'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: is_prime(result), lambda formula, result, context: is_close(result, (1.63661632336,1.1448, 1.0308, 0.9973, 0.9888, 0.9887, 0.9910, 0.9935, 0.9956, 0.9971))])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube819(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=lHJxZ7JOEwI'
        self.title = 'Mathematical Hugs (and Chiral Knots)'
        self.host = ['Ayliean MacDonald', 'Lorna MacDonald']
        self.date = '2022-06-21'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = 'knots'
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: None])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




class Youtube820(NumberCollection):
    def __init__(self, number_set_id=None):
        self.link = 'https://www.youtube.com/watch?v=k_TEoUF12Yk'
        self.title = 'Are there 10^272,000 Universes?'
        self.host = ['Tony Padilla']
        self.date = '2022-06-28'
        self.source = 'Numberphile'
        self.oeis = None
        self.wiki = None
        self.note = None
        self.number_set_id = number_set_id

    def contains(self, number):
        try:
            return any(t('', number, {'result': [number]}) for t in [lambda formula, result, context: result == 1e272_000])
        except (NameError, IndexError) as ex:
            print(self)
            raise ex
        except OverflowError as ex:
            return False




ALL_CLASS_NAMES = [Youtube0, Youtube1, Youtube2, Youtube3, Youtube4, Youtube5, Youtube6, Youtube7, Youtube8, Youtube9, Youtube10, Youtube11, Youtube12, Youtube13, Youtube14, Youtube15, Youtube16, Youtube17, Youtube18, Youtube19, Youtube20, Youtube21, Youtube22, Youtube23, Youtube24, Youtube25, Youtube26, Youtube27, Youtube28, Youtube29, Youtube30, Youtube31, Youtube32, Youtube33, Youtube34, Youtube35, Youtube36, Youtube37, Youtube38, Youtube39, Youtube40, Youtube41, Youtube42, Youtube43, Youtube44, Youtube45, Youtube46, Youtube47, Youtube48, Youtube49, Youtube50, Youtube51, Youtube52, Youtube53, Youtube54, Youtube55, Youtube56, Youtube57, Youtube58, Youtube59, Youtube60, Youtube61, Youtube62, Youtube63, Youtube64, Youtube65, Youtube66, Youtube67, Youtube68, Youtube69, Youtube70, Youtube71, Youtube72, Youtube73, Youtube74, Youtube75, Youtube76, Youtube77, Youtube78, Youtube79, Youtube80, Youtube81, Youtube82, Youtube83, Youtube84, Youtube85, Youtube86, Youtube87, Youtube88, Youtube89, Youtube90, Youtube91, Youtube92, Youtube93, Youtube94, Youtube95, Youtube96, Youtube97, Youtube98, Youtube99, Youtube100, Youtube101, Youtube102, Youtube103, Youtube104, Youtube105, Youtube106, Youtube107, Youtube108, Youtube109, Youtube110, Youtube111, Youtube112, Youtube113, Youtube114, Youtube115, Youtube116, Youtube117, Youtube118, Youtube119, Youtube120, Youtube121, Youtube122, Youtube123, Youtube124, Youtube125, Youtube126, Youtube127, Youtube128, Youtube129, Youtube130, Youtube131, Youtube132, Youtube133, Youtube134, Youtube135, Youtube136, Youtube137, Youtube138, Youtube139, Youtube140, Youtube141, Youtube142, Youtube143, Youtube144, Youtube145, Youtube146, Youtube147, Youtube148, Youtube149, Youtube150, Youtube151, Youtube152, Youtube153, Youtube154, Youtube155, Youtube156, Youtube157, Youtube158, Youtube159, Youtube160, Youtube161, Youtube162, Youtube163, Youtube164, Youtube165, Youtube166, Youtube167, Youtube168, Youtube169, Youtube170, Youtube171, Youtube172, Youtube173, Youtube174, Youtube175, Youtube176, Youtube177, Youtube178, Youtube179, Youtube180, Youtube181, Youtube182, Youtube183, Youtube184, Youtube185, Youtube186, Youtube187, Youtube188, Youtube189, Youtube190, Youtube191, Youtube192, Youtube193, Youtube194, Youtube195, Youtube196, Youtube197, Youtube198, Youtube199, Youtube200, Youtube201, Youtube202, Youtube203, Youtube204, Youtube205, Youtube206, Youtube207, Youtube208, Youtube209, Youtube210, Youtube211, Youtube212, Youtube213, Youtube214, Youtube215, Youtube216, Youtube217, Youtube218, Youtube219, Youtube220, Youtube221, Youtube222, Youtube223, Youtube224, Youtube225, Youtube226, Youtube227, Youtube228, Youtube229, Youtube230, Youtube231, Youtube232, Youtube233, Youtube234, Youtube235, Youtube236, Youtube237, Youtube238, Youtube239, Youtube240, Youtube241, Youtube242, Youtube243, Youtube244, Youtube245, Youtube246, Youtube247, Youtube248, Youtube249, Youtube250, Youtube251, Youtube252, Youtube253, Youtube254, Youtube255, Youtube256, Youtube257, Youtube258, Youtube259, Youtube260, Youtube261, Youtube262, Youtube263, Youtube264, Youtube265, Youtube266, Youtube267, Youtube268, Youtube269, Youtube270, Youtube271, Youtube272, Youtube273, Youtube274, Youtube275, Youtube276, Youtube277, Youtube278, Youtube279, Youtube280, Youtube281, Youtube282, Youtube283, Youtube284, Youtube285, Youtube286, Youtube287, Youtube288, Youtube289, Youtube290, Youtube291, Youtube292, Youtube293, Youtube294, Youtube295, Youtube296, Youtube297, Youtube298, Youtube299, Youtube300, Youtube301, Youtube302, Youtube303, Youtube304, Youtube305, Youtube306, Youtube307, Youtube308, Youtube309, Youtube310, Youtube311, Youtube312, Youtube313, Youtube314, Youtube315, Youtube316, Youtube317, Youtube318, Youtube319, Youtube320, Youtube321, Youtube322, Youtube323, Youtube324, Youtube325, Youtube326, Youtube327, Youtube328, Youtube329, Youtube330, Youtube331, Youtube332, Youtube333, Youtube334, Youtube335, Youtube336, Youtube337, Youtube338, Youtube339, Youtube340, Youtube341, Youtube342, Youtube343, Youtube344, Youtube345, Youtube346, Youtube347, Youtube348, Youtube349, Youtube350, Youtube351, Youtube352, Youtube353, Youtube354, Youtube355, Youtube356, Youtube357, Youtube358, Youtube359, Youtube360, Youtube361, Youtube362, Youtube363, Youtube364, Youtube365, Youtube366, Youtube367, Youtube368, Youtube369, Youtube370, Youtube371, Youtube372, Youtube373, Youtube374, Youtube375, Youtube376, Youtube377, Youtube378, Youtube379, Youtube380, Youtube381, Youtube382, Youtube383, Youtube384, Youtube385, Youtube386, Youtube387, Youtube388, Youtube389, Youtube390, Youtube391, Youtube392, Youtube393, Youtube394, Youtube395, Youtube396, Youtube397, Youtube398, Youtube399, Youtube400, Youtube401, Youtube402, Youtube403, Youtube404, Youtube405, Youtube406, Youtube407, Youtube408, Youtube409, Youtube410, Youtube411, Youtube412, Youtube413, Youtube414, Youtube415, Youtube416, Youtube417, Youtube418, Youtube419, Youtube420, Youtube421, Youtube422, Youtube423, Youtube424, Youtube425, Youtube426, Youtube427, Youtube428, Youtube429, Youtube430, Youtube431, Youtube432, Youtube433, Youtube434, Youtube435, Youtube436, Youtube437, Youtube438, Youtube439, Youtube440, Youtube441, Youtube442, Youtube443, Youtube444, Youtube445, Youtube446, Youtube447, Youtube448, Youtube449, Youtube450, Youtube451, Youtube452, Youtube453, Youtube454, Youtube455, Youtube456, Youtube457, Youtube458, Youtube459, Youtube460, Youtube461, Youtube462, Youtube463, Youtube464, Youtube465, Youtube466, Youtube467, Youtube468, Youtube469, Youtube470, Youtube471, Youtube472, Youtube473, Youtube474, Youtube475, Youtube476, Youtube477, Youtube478, Youtube479, Youtube480, Youtube481, Youtube482, Youtube483, Youtube484, Youtube485, Youtube486, Youtube487, Youtube488, Youtube489, Youtube490, Youtube491, Youtube492, Youtube493, Youtube494, Youtube495, Youtube496, Youtube497, Youtube498, Youtube499, Youtube500, Youtube501, Youtube502, Youtube503, Youtube504, Youtube505, Youtube506, Youtube507, Youtube508, Youtube509, Youtube510, Youtube511, Youtube512, Youtube513, Youtube514, Youtube515, Youtube516, Youtube517, Youtube518, Youtube519, Youtube520, Youtube521, Youtube522, Youtube523, Youtube524, Youtube525, Youtube526, Youtube527, Youtube528, Youtube529, Youtube530, Youtube531, Youtube532, Youtube533, Youtube534, Youtube535, Youtube536, Youtube537, Youtube538, Youtube539, Youtube540, Youtube541, Youtube542, Youtube543, Youtube544, Youtube545, Youtube546, Youtube547, Youtube548, Youtube549, Youtube550, Youtube551, Youtube552, Youtube553, Youtube554, Youtube555, Youtube556, Youtube557, Youtube558, Youtube559, Youtube560, Youtube561, Youtube562, Youtube563, Youtube564, Youtube565, Youtube566, Youtube567, Youtube568, Youtube569, Youtube570, Youtube571, Youtube572, Youtube573, Youtube574, Youtube575, Youtube576, Youtube577, Youtube578, Youtube579, Youtube580, Youtube581, Youtube582, Youtube583, Youtube584, Youtube585, Youtube586, Youtube587, Youtube588, Youtube589, Youtube590, Youtube591, Youtube592, Youtube593, Youtube594, Youtube595, Youtube596, Youtube597, Youtube598, Youtube599, Youtube600, Youtube601, Youtube602, Youtube603, Youtube604, Youtube605, Youtube606, Youtube607, Youtube608, Youtube609, Youtube610, Youtube611, Youtube612, Youtube613, Youtube614, Youtube615, Youtube616, Youtube617, Youtube618, Youtube619, Youtube620, Youtube621, Youtube622, Youtube623, Youtube624, Youtube625, Youtube626, Youtube627, Youtube628, Youtube629, Youtube630, Youtube631, Youtube632, Youtube633, Youtube634, Youtube635, Youtube636, Youtube637, Youtube638, Youtube639, Youtube640, Youtube641, Youtube642, Youtube643, Youtube644, Youtube645, Youtube646, Youtube647, Youtube648, Youtube649, Youtube650, Youtube651, Youtube652, Youtube653, Youtube654, Youtube655, Youtube656, Youtube657, Youtube658, Youtube659, Youtube660, Youtube661, Youtube662, Youtube663, Youtube664, Youtube665, Youtube666, Youtube667, Youtube668, Youtube669, Youtube670, Youtube671, Youtube672, Youtube673, Youtube674, Youtube675, Youtube676, Youtube677, Youtube678, Youtube679, Youtube680, Youtube681, Youtube682, Youtube683, Youtube684, Youtube685, Youtube686, Youtube687, Youtube688, Youtube689, Youtube690, Youtube691, Youtube692, Youtube693, Youtube694, Youtube695, Youtube696, Youtube697, Youtube698, Youtube699, Youtube700, Youtube701, Youtube702, Youtube703, Youtube704, Youtube705, Youtube706, Youtube707, Youtube708, Youtube709, Youtube710, Youtube711, Youtube712, Youtube713, Youtube714, Youtube715, Youtube716, Youtube717, Youtube718, Youtube719, Youtube720, Youtube721, Youtube722, Youtube723, Youtube724, Youtube725, Youtube726, Youtube727, Youtube728, Youtube729, Youtube730, Youtube731, Youtube732, Youtube733, Youtube734, Youtube735, Youtube736, Youtube737, Youtube738, Youtube739, Youtube740, Youtube741, Youtube742, Youtube743, Youtube744, Youtube745, Youtube746, Youtube747, Youtube748, Youtube749, Youtube750, Youtube751, Youtube752, Youtube753, Youtube754, Youtube755, Youtube756, Youtube757, Youtube758, Youtube759, Youtube760, Youtube761, Youtube762, Youtube763, Youtube764, Youtube765, Youtube766, Youtube767, Youtube768, Youtube769, Youtube770, Youtube771, Youtube772, Youtube773, Youtube774, Youtube775, Youtube776, Youtube777, Youtube778, Youtube779, Youtube780, Youtube781, Youtube782, Youtube783, Youtube784, Youtube785, Youtube786, Youtube787, Youtube788, Youtube789, Youtube790, Youtube791, Youtube792, Youtube793, Youtube794, Youtube795, Youtube796, Youtube797, Youtube798, Youtube799, Youtube800, Youtube801, Youtube802, Youtube803, Youtube804, Youtube805, Youtube806, Youtube807, Youtube808, Youtube809, Youtube810, Youtube811, Youtube812, Youtube813, Youtube814, Youtube815, Youtube816, Youtube817, Youtube818, Youtube819, Youtube820]
ALL_TESTS = [t() for t in ALL_CLASS_NAMES]