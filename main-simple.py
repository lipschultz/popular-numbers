import itertools
from pathlib import Path
from typing import List

from tqdm import tqdm

import youtube
from popularity import database


class irange:
    def __init__(self, start: int, end: int):
        if not isinstance(start, int):
            raise TypeError(f"'{type(start)}' object cannot be interpreted as an integer")
        if not isinstance(end, int):
            raise TypeError(f"'{type(end)}' object cannot be interpreted as an integer")

        self._range = range(start, end)

    def __len__(self):
        return len(self._range)

    def __iter__(self):
        return (complex(0, v) for v in self._range)


class crange:
    def __init__(self, real_values: range, imag_values: irange):
        self._reals = real_values
        self._imags = imag_values

    def __len__(self):
        return len(self._reals) * len(self._imags)

    def __iter__(self):
        return (
            r + i if i.imag != 0 else r
            for r, i in itertools.product(self._reals, self._imags)
        )


def initialize_database(loaded_tests, db_url):
    needs_initialization = not Path(DB_URL).exists()

    conn = database.connect(db_url)
    if needs_initialization:
        database.init_db(conn)

    sources_to_ids = database.youtube_sources_to_id(conn, loaded_tests)

    for test in loaded_tests:
        test.number_set_id = sources_to_ids[test.link]

    conn.close()


def run_test_on_all_numbers(number_set_tester, all_numbers) -> List[database.NumberSetElement]:
    results = []
    for number in tqdm(all_numbers, desc=number_set_tester.title, position=1, leave=False):
        try:
            if number_set_tester.contains(number):
                real, imag = (number.real, number.imag) if isinstance(number, complex) else (number, 0)
                results.append(database.NumberSetElement(real, imag, number_set_tester.number_set_id))
        except TypeError as ex:
            print(number_set_tester)
            print(number)
            raise ex
    return results


def main(number_generator):
    initialize_database(youtube.ALL_TESTS, DB_URL)

    db_conn = database.connect(DB_URL)
    for test in tqdm(youtube.ALL_TESTS, desc='Running tests', position=0, leave=True):
        results = run_test_on_all_numbers(test, number_generator)
        database.record_number_set_members(results, db_conn)
    db_conn.close()


if __name__ == '__main__':
    # DB_URL = 'run-0.db'
    # reals = range(0, 1_000+1)

    DB_URL = 'run-1.db'
    reals = range(1_000+1, 2_000+1)

    imags = irange(0, 10_000+1)

    complexes = crange(reals, imags)
    main(complexes)
