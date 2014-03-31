import argparse
from parser.parser import parse_file
from lepl import * 

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Process some integers.')
    p.add_argument('files', metavar='FILE', type=str, nargs='+',
                               help='input filename')
    args = p.parse_args()

    for f in args.files:
        parse_file(f)
