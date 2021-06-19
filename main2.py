import sqlite3

import youtube
from popularity import database
from popularity import load
from popularity import compute_popularity
from popularity.compute_popularity import loop_over_tests, loop_over_tests_parallel
from popularity.number_generator import SimpleNumberGenerator as NumberGenerator


def main():
    db_url = r'results-map_async,p3.db'
    reals_run = NumberGenerator(
        0, 0, 1,  # Real
        -10_000, -9_999, 2,  # Imaginary
    )

    conn = database.connect(db_url)
    database.init_db(conn)
    loaded_videos = youtube.ALL_TESTS
    sources_to_ids = database.youtube_sources_to_id(conn, loaded_videos)
    conn.close()

    print('Computing results')
    results = compute_popularity.loop_over_tests_map_async(reals_run, sources_to_ids, db_url)
    print('Computing results: done')

    return results


if __name__ == '__main__':
    results = main()
