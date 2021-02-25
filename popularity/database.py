import sqlite3
from pathlib import Path


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


