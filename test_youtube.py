import math
from collections import defaultdict

from popularity import numeric_tools
from popularity.compute_popularity import single_process


def main():
    youtube_file = 'data/youtube.json'
    any_source_to_id = defaultdict(lambda: 1)

    numbers = [
        0,
        1,
        2,
        numeric_tools.GOLDEN_RATIO,
        numeric_tools.PRIME_NUMBERS[15],
        numeric_tools.FIBONACCI_NUMBERS[15],
        numeric_tools.LUCAS_NUMBERS[15],
        math.pi,
        math.e,
        math.inf,
        math.pi + 1.643e-8,
        math.e + 1.643e-8,
        0.5,
        13.7,
        # 1e-35,
        # 1e35,
        -1,
        -2,
        -0.5,
        -13.7,
        # -1e-35,
        # -1e35,
        complex(3, 1),
        88,
        complex(6, 17.079468445347132),
        45,
        int('04321'),
        # 53177187714,
        # 57316483775,
    ]

    run = iter(numbers)

    results = single_process(youtube_file, run, any_source_to_id, None)
    return results


if __name__ == '__main__':
    results = main()
