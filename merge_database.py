import sqlite3
from pathlib import Path

from tqdm import tqdm

from popularity import database, load


def translate_database(conn_old, conn_new, link_id_mapper):
    with conn_new:
        for row in tqdm(conn_old.execute("SELECT link, real, imag FROM popularity;")):
            new_id = link_id_mapper[row['link']]
            _ = conn_new.execute("INSERT INTO NumberSetMembers(number_set_id, real, imag) VALUES(?, ?, ?) ON CONFLICT DO NOTHING;", (new_id, row['real'], row['imag']))


def main():
    youtube_file = 'data/youtube.json'

    out_db = 'merged.db'
    
    initialize_database = not Path(out_db).exists()
    
    conn = database.connect(out_db)
    if initialize_database:
        database.init_db(conn)
    link_id_mapper = database.youtube_sources_to_id(conn, youtube_file)

    conn.close()
    return link_id_mapper


if __name__ == '__main__':
    results = main()
