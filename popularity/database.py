import sqlite3
from collections import namedtuple
from pathlib import Path
from typing import List

from dateutil.parser import parse as date_parse
from tqdm import tqdm


NumberSetElement = namedtuple('NumberSetElement', ['real', 'imag', 'number_set_id'])


def connect(filename, readonly=False, row_factory=sqlite3.Row):
    uri_args = {
        'mode': 'ro' if readonly else 'rwc'
    }
    uri_args_str = '&'.join(f'{k}={v}' for k, v in uri_args.items())

    filepath = Path(filename)
    conn = sqlite3.connect(f'file:{filepath}?{uri_args_str}', uri=True)

    conn.row_factory = row_factory
    return conn


def init_db(conn):
    with conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS Collections (
            id INTEGER PRIMARY KEY,
            name TEXT,
            UNIQUE (name)
        );''')  # name in "youtube", "oeis"

        conn.execute('''
        CREATE TABLE IF NOT EXISTS NumberSets (
            id INTEGER PRIMARY KEY,
            collection_id INTEGER REFERENCES Collections(id),
            label TEXT,
            UNIQUE (collection_id, label)
        );''')  # label is OEIS's Anumber or Youtube's link

        conn.execute('''
        CREATE TABLE IF NOT EXISTS YoutubeNumberSets (
            number_set_id INTEGER REFERENCES NumberSets(id),
            title TEXT,
            source TEXT,
            date DATE
        );''')  # source is "Numberphile", "standupmaths"

        conn.execute('''
        CREATE TABLE IF NOT EXISTS YoutubeHosts (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        );''')

        conn.execute('''
        CREATE TABLE IF NOT EXISTS YoutubeNumberSetHosts (
            number_set_id INTEGER REFERENCES NumberSets(id),
            youtube_host_id INTEGER REFERENCES YoutubeHosts(id)
        );''')

        conn.execute('''
        CREATE TABLE IF NOT EXISTS NumberSetMembers (
            number_set_id INTEGER REFERENCES NumberSets(id),
            real NUMERIC,
            imag NUMERIC,
            PRIMARY KEY (real, imag, number_set_id)
        );''')


def get_table_id(conn, table, name, create=True):
    with conn:
        for row in conn.execute(f"SELECT id FROM {table} WHERE name=?;", (name,)):
            return row['id']

        if create:
            res = conn.execute(f"INSERT INTO {table}(name) VALUES (?);", (name,))
            return res.lastrowid
        else:
            return None


def get_collection_id(conn, name, create=True):
    return get_table_id(conn, 'Collections', name, create=create)


def get_youtube_host_id(conn, name, create=True):
    return get_table_id(conn, 'YoutubeHosts', name, create=create)


def youtube_sources_to_id(conn, loaded_videos=None, create=True):
    youtube_collection_id = get_collection_id(conn, 'youtube', create=create)

    with conn:
        link_to_id = {
            row['label']: row['id']
            for row in conn.execute("SELECT id, label FROM NumberSets WHERE collection_id=?;", (youtube_collection_id,))
        }

    loaded_videos_to_add = [v for v in loaded_videos if v.link not in link_to_id]
    if create:
        with conn:
            for video in tqdm(loaded_videos_to_add, desc='Creating NumberSet table'):
                try:
                    cursor = conn.execute("INSERT INTO NumberSets(collection_id, label) VALUES(?, ?);", (youtube_collection_id, video.link))
                    number_set_id = cursor.lastrowid
                except sqlite3.IntegrityError as ex:
                    if str(ex).startswith('UNIQUE constraint failed'):
                        continue

                iso_date = date_parse(video.date).date().isoformat()
                conn.execute("INSERT INTO YoutubeNumberSets(number_set_id, title, source, date) VALUES (?, ?, ?, ?);", (number_set_id, video.title, video.source, iso_date))

                for host_name in video.host:
                    host_id = get_youtube_host_id(conn, host_name, create=create)
                    conn.execute("INSERT INTO YoutubeNumberSetHosts(number_set_id, youtube_host_id) VALUES(?, ?);", (number_set_id, host_id))

                link_to_id[video.link] = number_set_id
    return link_to_id


def record_number_set_members(members: List[NumberSetElement], db_conn, *, n_attempts=5):
    if db_conn is None:
        return
    if len(members) == 0:
        return

    n_failures = 0
    last_exception = None
    while n_failures < n_attempts:
        try:
            with db_conn:
                db_conn.executemany(
                    f'''
                        INSERT INTO NumberSetMembers(real, imag, number_set_id)
                        VALUES (?, ?, ?)
                        ON CONFLICT DO NOTHING
                    ''',
                    members
                )
                return
        except sqlite3.ProgrammingError as ex:
            print(members)
            print(len(members))
            print(ex)
            raise
        except sqlite3.OperationalError as ex:
            time.sleep(1)
            n_failures += 1
            last_exception = ex
    raise last_exception
