import sqlite3

from popularity import database
from popularity import load
from popularity import compute_popularity
from popularity.compute_popularity import loop_over_tests, loop_over_tests_parallel
from popularity.number_generator import SimpleNumberGenerator as NumberGenerator


def main():
    youtube_file = 'data/youtube.json'

    db_url = r'results.db'
    reals_run = NumberGenerator(
        -10_000, -9_999, 1,  # Real
        0, 0, 1,  # Imaginary
    )

    conn = database.connect(db_url)
    database.init_db(conn)
    loaded_videos = load.YoutubeVideo.load_file(youtube_file)
    sources_to_ids = database.youtube_sources_to_id(conn, loaded_videos)
    conn.close()

    results = compute_popularity.loop_over_tests_map_async(reals_run, sources_to_ids, db_url)
    # results = loop_over_tests(reals_run, sources_to_ids, db_url)

    return results


if __name__ == '__main__':
    results = main()
