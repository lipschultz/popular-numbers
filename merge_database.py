import sys

from tqdm import tqdm

from popularity import database


def main():
    final_db = sys.argv[1]
    final_conn = database.connect(final_db)
    for other_db in sys.argv[2:]:
        other_conn = database.connect(other_db)
        database.merge_db_number_set_members(other_conn, final_conn)
        other_conn.close()
    final_conn.close()


if __name__ == '__main__':
    main()
