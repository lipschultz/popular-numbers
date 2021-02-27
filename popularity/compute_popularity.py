import sqlite3
import time
from typing import List, Iterable

from tqdm import tqdm

from popularity import database
from popularity import load
from popularity.number_generator import SimpleNumberGenerator
SENTINEL_VALUE = 'STOP'


def run_number_on_all_tests(number, all_tests) -> List[database.NumberSetElement]:
    results = []
    for fact in all_tests:
        try:
            if fact.contains(number):
                real, imag = (number.real, number.imag) if isinstance(number, complex) else (number, 0)
                results.append(database.NumberSetElement(real, imag, fact.number_set_id))
        except TypeError as ex:
            print(fact)
            print(number)
            raise ex
    return results


def loop_over_numbers(test_json_file, numbers: SimpleNumberGenerator, sources_to_ids, db_conn) -> List[database.NumberSetElement]:
    tests = load.YoutubeVideo.load_file(test_json_file)
    for test in tests:
        test.number_set_id = sources_to_ids[test.link]

    all_results = []
    print('processing numbers')
    for number in tqdm(numbers):
        results = run_number_on_all_tests(number, tests)
        database.record_number_set_members(results, db_conn)
        all_results.extend(results)
    return all_results


def run_test_on_all_numbers(number_set_tester, all_numbers) -> List[database.NumberSetElement]:
    results = []
    for number in iter(all_numbers):
        try:
            if number_set_tester.contains(number):
                real, imag = (number.real, number.imag) if isinstance(number, complex) else (number, 0)
                results.append(database.NumberSetElement(real, imag, number_set_tester.number_set_id))
        except TypeError as ex:
            print(fact)
            print(number)
            raise ex
    return results


def loop_over_tests(test_json_file, numbers: SimpleNumberGenerator, sources_to_ids, db_conn) -> List[database.NumberSetElement]:
    print('loading tests')
    tests = load.YoutubeVideo.load_file(test_json_file)
    for test in tests:
        test.number_set_id = sources_to_ids[test.link]

    all_results = []
    print('processing numbers')
    for test in tqdm(tests):
        results = run_test_on_all_numbers(test, numbers)
        database.record_number_set_members(results, db_conn)
        all_results.extend(results)
    return all_results
