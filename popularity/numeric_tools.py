import functools
import itertools
import math
import time
from fractions import Fraction
from pathlib import Path


def is_int(val):
    """ Returns True if val is an int or a float with 0 fractional part """
    return isinstance(val, int) or (isinstance(val, float) and val % 1 == 0)


def is_rational(val):
    """
    Returns True if val is an int or float and not irrational.

    Determining irrationality is done through the is_irrational method.
    """
    return isinstance(val, (int, float)) and not is_irrational(val)


def is_irrational(val):
    """
    Returns True if val is irrational.

    Irrationality is determined by whether val is transcendental (as
    determined by is_transcendental) or sqrt(2) or golden ratio.
    """
    return is_transcendental(val) or val in {2 ** .5, GOLDEN_RATIO}


def is_transcendental(val):
    """ Returns True if val is transcendental (i.e. pi or e). """
    return val in (math.pi, math.e)


def is_real(val):
    """ Returns True if val is int or float. """
    return isinstance(val, (int, float))


def is_complex(val):
    """ Returns True if val is complex. """
    return isinstance(val, complex)


def is_algebraic(val):
    return (is_real(val) or is_complex(val)) and not is_transcendental(val)


def is_surreal(val):
    """ Returns True if val is surreal (currently always returns False). """
    return False


def is_number(val):
    """ Returns True if val is int, float, or complex. """
    return isinstance(val, (int, float, complex))


def is_error(val):
    """ Returns True if val is a ComputationError. """
    return isinstance(val, Exception)


GOLDEN_RATIO = (1 + 5 ** 0.5) / 2
GRAHAMS_NUMBER = False
I = complex(0, 1)

PI_DIGITS = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2,
             6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3,
             9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0,
             7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4,
             8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9, 8, 2, 1, 4
             )


def is_prime(n):
    """
    Returns True if number is a prime number.

    Makes use of a deterministic variant of the Miller-Rabin Primality Test
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants
    """
    if not is_int(n):
        return False

    n = int(n)
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False

    all_witnesses = [
        (2047, [2]),
        (1_373_653, [2, 3]),
        (9_080_191, [31, 73]),
        (25_326_001, [2, 3, 5]),
        (3_215_031_751, [2, 3, 5, 7]),
        (4_759_123_141, [2, 7, 61]),
        (1_122_004_669_633, [2, 13, 23, 1662803]),
        (2_152_302_898_747, [2, 3, 5, 7, 11]),
        (3_474_749_660_383, [2, 3, 5, 7, 11, 13]),
        (341_550_071_728_321, [2, 3, 5, 7, 11, 13, 17]),
        (3_825_123_056_546_413_051, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (318_665_857_834_031_151_167_461, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]),
        (3_317_044_064_679_887_385_961_981, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]),
    ]
    witness_candidates = (w for max_val, w in all_witnesses if n < max_val)
    witnesses = next(witness_candidates)
    n1 = n - 1

    d = n1
    r = 0
    res, rem = divmod(d, 2)
    while rem == 0:
        r += 1
        d = res
        res, rem = divmod(d, 2)

    for witness in witnesses:
        x = witness ** d % n
        if x == 1 or x == n1:
            continue
        #
        is_composite = True
        for _ in range(r-1):
            x = x ** 2 % n
            if x == n1:
                is_composite = False
                break
        if is_composite:
            return False

    return True


PRIME_NUMBERS = [int(n) for n in (Path(__file__).parent.parent / 'data' / 'primes.csv').read_text().split(',')]


FACTORS_ALL = 'all'
FACTORS_PROPER = 'proper'
FACTORS_PRIME = 'prime'


def factors(num, form=FACTORS_PROPER):
    """
    Return a list of factors for the provided number.

    If form is FACTORS_PRIME, then the list will only contain the prime
    factors of num.  The product of the values in the list will always
    return num.  That is, if the number is a product of more than one of
    the same prime (e.g. 12 = 2*2*3), then the list will contain those
    duplicates (e.g. [2, 2, 3] in the example).

    If form is FACTORS_ALL, then the list will contain all positive
    integers that exactly divide num.  For example, with num=12, the
    list returned is [1, 2, 3, 4, 12].

    If form is FACTORS_PROPER (default), then the list will be the same
    as FACTORS_ALL, except the list will not include num.  So, for
    num=12, the list returned would be [1, 2, 3, 4].

    If num is not an integer (as determined by is_int) greater than 1,
    return empty list.
    """
    if not is_int(num) or num < 2:
        return []
    if form == FACTORS_PRIME:
        primes = []
        i = 2
        while num % i == 0:
            primes.append(i)
            num /= i
        i = 3
        while num > 1:
            while num % i == 0:
                primes.append(i)
                num /= i
            i += 2
        return primes
    else:
        all_factors = functools.reduce(list.__add__,
                                       ([i, num // i] for i in range(1, int(num ** 0.5) + 1) if num % i == 0)
                                       )
        if form == FACTORS_PROPER:
            all_factors.remove(num)
        return all_factors


FIBONACCI_NUMBERS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                     377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                     28657, 46368, 75025, 121393, 196418, 317811, 514229,
                     832040, 1346269
                     ]
LUCAS_NUMBERS = (2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,
                 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603, 64079,
                 103682, 167761, 271443, 439204, 710647, 1149851, 1860498,
                 3010349, 4870847, 7881196, 12752043, 20633239, 33385282
                 )


def is_subsequence_of(needle, haystack):
    """
    Returns True if needle occurs as a consecutive subsequence in haystack.

    Both needle and haystack must be ordered containers.  The values in
    needle must appear in haystack in the order they appear in needle
    and must be consecutive in haystack.

    For example, with needle=[1,2,3] and haystack=[1,1,2,3,4], the
    function returns True since needle starts at index 1 in haystack.

    With needle=[1,2,4] and haystack=[1,1,2,3,4], the function returns
    False since, although the values do appear in haystack in the
    correct order, they are not consecutive.

    An empty needle will always return False.
    """
    if len(needle) == 0:
        return False
    for offset in (i for i, x in enumerate(haystack) if x == needle[0]):
        if offset + len(needle) > len(haystack):
            return False

        matches = [needle[i] == haystack[offset + i] for i in range(1, len(needle))]

        if len(matches) == len(needle) - 1 and all(matches):
            return True

    return False


def is_close(num1, num2, threshold=1e-5, method='raw'):
    """
    Returns True if num1 is within threshold of num2.

    If method is 'raw', then the closeness is determined by the absolute
    value of the difference between num1 and num2.

    If method is 'pct', then the absolute value of percent difference is
    calculated and used.

    num1 and num2 can be iterable.  If one is iterable, then as long as
    one value in the iterable object is close to the other number, the
    function returns True.  If both are iterable, then as long as one
    value in num1 is close to one value in num2, the function returns
    True.
    """
    if isinstance(num1, Exception) or isinstance(num2, Exception):
        return False
    elif hasattr(num1, '__iter__'):
        return any(is_close(n, num2, threshold) for n in num1)
    elif hasattr(num2, '__iter__'):
        return any(is_close(num1, n, threshold) for n in num2)
    elif ((isinstance(num1, complex) or isinstance(num2, complex))
          and not isinstance(num1, type(num2))):
        return False
    else:
        if method == 'pct':
            if num1 == num2 and num1 == 0:
                return True
            else:
                return abs(num1 - num2) / max([abs(v) for v in (num1, num2) if v != 0]) < threshold
        else:
            return abs(num1 - num2) < threshold


def farey_addition(context):
    """
    Perform Farey addition on previous and previous-third result and
    return True if it equals the previous-second result.
    """
    if len(context['result']) < 3 or any(not is_rational(r) for r in context['result'][-3:]):
        return False
    first = Fraction(context['result'][-3]).limit_denominator(234)
    second = Fraction(context['result'][-2]).limit_denominator(234)
    third = Fraction(context['result'][-1]).limit_denominator(234)
    return Fraction(first.numerator + third.numerator,
                    first.denominator + third.denominator
                    ) == second


def int_to_digits(result, as_type=int):
    """ Convert result into a list of digits. """
    if as_type == int:
        return [result // 10 ** i % 10 for i in range(math.ceil(math.log(result, 10)))]
    else:
        return list(str(result))


def vampire(result):
    """
    Returns True if result is a Vampire number.

    A vampire number is an integer whose digits, when used to form two
    integers (of equal length) that are then multiplied together, give
    back the original number, e.g. 1260 = 21*60.
    """
    digits = int_to_digits(result, str)
    result_size = len(digits)
    partition_template = [1] * (result_size // 2) + [0] * (result_size // 2)
    partitions = set([v for v in itertools.permutations(partition_template)])
    for part in partitions:
        fang1 = int(''.join(itertools.compress(digits, part)))
        fang2 = int(''.join(itertools.compress(digits, [-1 * v + 1 for v in part])))
        print(fang1, '*', fang2, '=', fang1 * fang2, '?=', result)
        if fang1 * fang2 == result:
            return True
    return False


def double_factorial(n):
    if n == 0:
        return 1
    elif is_int(n):
        if n > 0:
            return functools.reduce(int.__mul__, range(n, 0, -2))
        else:
            return double_factorial(n + 2) / (n + 2)
    else:
        raise ValueError(f'Unsupported value: {n}')
