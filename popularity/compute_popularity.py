import sqlite3
import time
from collections import namedtuple
from multiprocessing import Process, Queue, cpu_count
from typing import List, Iterable

from tqdm import tqdm

from popularity import load

PopularityResults = namedtuple('PopularityResults', ['real', 'imag', 'link', 'source'])
SENTINEL_VALUE = 'STOP'


def process_number(number, yt) -> List[PopularityResults]:
    results = []
    for fact in yt:
        try:
            if fact.contains(number):
                real, imag = (number.real, number.imag) if isinstance(number, complex) else (number, 0)
                results.append(PopularityResults(real, imag, fact.link, fact.source))
        except TypeError as ex:
            print(fact)
            print(number)
            raise ex
    return results


def record_results(results: List[PopularityResults], db_conn):
    if db_conn is None:
        return

    n_failures = 0
    last_exception = None
    while n_failures < 5:
        try:
            with db_conn:
                db_conn.executemany(
                    f'''
                        INSERT INTO popularity({', '.join(PopularityResults._fields)})
                        VALUES ({', '.join(['?'] * len(PopularityResults._fields))})
                        ON CONFLICT DO NOTHING
                    ''',
                    results
                )
                return
        except sqlite3.OperationalError as ex:
            time.sleep(1)
            n_failures += 1
            last_exception = ex
    raise last_exception


def single_process(test_json_file, numbers: Iterable, db_conn) -> List[PopularityResults]:
    tests = load.YoutubeVideo.load_file(test_json_file)
    results = []
    for number in tqdm(numbers):
        results.extend(process_number(number, tests))
    record_results(results, db_conn)
    return results


def mp_queue_worker(test_json_file, task_queue, result_queue):
    tests = load.YoutubeVideo.load_file(test_json_file)
    for num in iter(task_queue.get, SENTINEL_VALUE):
        result_queue.put(process_number(num, tests))
    result_queue.put(SENTINEL_VALUE)
    print('Queue worker ready to stop')


def mp_consume_processed_results(db_url, result_queue, n_stops_expected):
    db_conn = sqlite3.connect(db_url)
    n_stops_encountered = 0
    n_records = 0
    while n_stops_encountered < n_stops_expected:
        result_list = result_queue.get()
        if result_list == SENTINEL_VALUE:
            n_stops_encountered += 1
        else:
            record_results(result_list, db_conn)
            n_records += len(result_list)
            if n_records >= 1000:
                print('Recording results')
                db_conn.commit()
                n_records = 0
    db_conn.commit()
    db_conn.close()
    print('Consumer worker ready to stop')


def mp_queue(test_json_file, numbers: Iterable, db_url):
    total_start_time = time.time()
    n_processes = cpu_count() // 2

    task_queue = Queue(1000)
    result_queue = Queue(10_000)

    print('Starting processes:', n_processes)
    processors = [
        Process(target=mp_queue_worker, args=(test_json_file, task_queue, result_queue))
        for _ in range(n_processes)
    ]
    for proc in processors:
        proc.start()

    consumer_process = Process(target=mp_consume_processed_results, args=(db_url, result_queue, n_processes))
    consumer_process.start()

    for number in tqdm(numbers):
        task_queue.put(number)

    print('Sending stop to queue workers')
    for _ in range(n_processes):
        task_queue.put(SENTINEL_VALUE)

    for i, proc in enumerate(processors):
        proc.join()
        print(f'Ended process {i}')

    consumer_process.join()
    print('Ended consumer')

    print('Closing task queue')
    task_queue.close()
    task_queue.join_thread()
    print('Closing result queue')
    result_queue.close()
    result_queue.join_thread()

    print('Recording final results')
    print('total runtime:', time.time() - total_start_time)
    return []
