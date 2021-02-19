import sqlite3
from multiprocessing import freeze_support

from popularity.compute_popularity import single_process
from popularity.number_generator import NumberGenerator


def main():
    youtube_file = 'data/youtube.json'

    db_url = r'results.db'
    reals_run = NumberGenerator(
        -10_000, -9_999, 2,  # Real
        0, 0, 1,  # Imaginary
        db_url=db_url
    )

    imaginary_run = NumberGenerator(
        0, 0, 1,  # Real
        -10_000, -9_999, 2,  # Imaginary
        db_url=db_url
    )

    complex_run = NumberGenerator(-10_000, 10_000, 2, db_url=db_url)

    run_pie = NumberGenerator(1.7, 4.2, 5, 0, 0, 0, skip=reals_run)

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

    results = single_process(youtube_file, reals_run, conn)
    conn.close()

    return results


if __name__ == '__main__':
    freeze_support()
    results = main()
