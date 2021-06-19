import multiprocessing
import sqlite3
import time
from typing import List, Iterable

from tqdm import tqdm

from popularity import database
from popularity import load
from popularity.number_generator import SimpleNumberGenerator
import youtube


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
            print(number_set_tester)
            print(number)
            raise ex
    return results


def run_test_on_all_numbers_one_arg(arg):
    return run_test_on_all_numbers(arg[0], arg[1])

# def loop_over_tests(test_json_file, numbers: SimpleNumberGenerator, sources_to_ids, db_conn) -> List[database.NumberSetElement]:
    # print('loading tests')
    # tests = load.YoutubeVideo.load_file(test_json_file)
    # for test in tests:
        # test.number_set_id = sources_to_ids[test.link]

    # all_results = []
    # print('processing numbers')
    # for test in tqdm(tests):
        # results = run_test_on_all_numbers(test, numbers)
        # database.record_number_set_members(results, db_conn)
        # all_results.extend(results)
    # return all_results


def loop_over_tests(numbers: SimpleNumberGenerator, sources_to_ids, db_url) -> List[database.NumberSetElement]:
    tests = [t() for t in youtube.ALL_CLASS_NAMES]
    for test in tests:
        test.number_set_id = sources_to_ids[test.link]

    db_conn = database.connect(db_url)
    all_results = []
    for test in tests:
        results = run_test_on_all_numbers(test, numbers)
        database.record_number_set_members(results, db_conn)
        all_results.extend(results)
    db_conn.close()

    return all_results


def loop_over_tests_parallel(numbers: SimpleNumberGenerator, sources_to_ids, db_url) -> List[database.NumberSetElement]:
    tests = [t() for t in youtube.ALL_CLASS_NAMES]
    for test in tests:
        test.number_set_id = sources_to_ids[test.link]

    arguments = [(test, numbers) for test in tests]

    def record_result(results):
        db_conn = database.connect(db_url)
        for result in results:
            database.record_number_set_members(result, db_conn)
        db_conn.close()

    with multiprocessing.Pool(processes=4) as pool:
        all_results = pool.starmap_async(run_test_on_all_numbers, arguments, chunksize=10, callback=record_result)
        all_results = all_results.get()

    # all_results = []
    # print('processing numbers')
    # for test in tqdm(tests):
        # results = run_test_on_all_numbers(test, numbers)
        # database.record_number_set_members(results, db_conn)
        # all_results.extend(results)
    return all_results


def loop_over_tests_map_async(numbers: SimpleNumberGenerator, sources_to_ids, db_url) -> List[database.NumberSetElement]:
    tests = [t() for t in youtube.ALL_CLASS_NAMES]
    for test in tests:
        test.number_set_id = sources_to_ids[test.link]

    arguments = [(test, numbers) for test in tests]

    def record_result(results):
        db_conn = database.connect(db_url)
        for result in results:
            database.record_number_set_members(result, db_conn)
        db_conn.close()

    with multiprocessing.Pool(processes=3) as pool:
        all_results = pool.map_async(run_test_on_all_numbers_one_arg, arguments)
        all_results = all_results.get()
        record_result(all_results)
    return all_results
