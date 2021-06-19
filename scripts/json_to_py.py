import os
import sys

sys.path.insert(0, '.')

from popularity.load import youtube_json_to_py


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Convert YouTube JSON file to python file')
    parser.add_argument('infile', help='JSON file to convert')
    parser.add_argument('outfile', help='Python file to save to')

    args = parser.parse_args()
    youtube_json_to_py(args.infile, args.outfile)

