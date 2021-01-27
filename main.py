import sqlite3
import sqlite3
import time
from collections import namedtuple
from multiprocessing import freeze_support, Process, Queue, cpu_count
from typing import List

from tqdm import tqdm

from popularity import load
from popularity.number_generator import NumberGenerator


def main():
    youtube_file = 'data/youtube.json'

    db_url = r'results-negative.db'
    run0 = NumberGenerator(-10_000, -9_999, 2,  # Real
                           # -10_000, 10_000, 2,  # Imaginary
                           db_url=db_url)

    # db_url = r'D:\results-positive.db'
    # run0 = NumberGenerator(9_998, 10_000, 2,  # Real
    #                        -10_000, 10_000, 2,  # Imaginary
    #                        db_url=db_url)

    conn = sqlite3.connect(db_url)
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS popularity (
            real NUMERIC,
            imag NUMERIC,
            link TEXT,
            source TEXT,
            PRIMARY KEY (real, imag, link)
        );''')


    # run0 = NumberGenerator(-10_000, 10_000, 2, db_url=db_url)
    # run_pie = NumberGenerator(1.7, 4.2, 5, 0, 0, 0, skip=run0)

    results = single_process(youtube_file, run0, conn)
    conn.close()
    # results = mp_queue(youtube_file, run0, db_url)
    return results


if __name__ == '__main__':
    freeze_support()
    results = main()
