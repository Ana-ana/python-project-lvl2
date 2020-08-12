import argparse
import json
import difflib
from pathlib import Path

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('--f', '--format',
                    metavar='FORMAT',
                    help='set format of output')


def main():
    args = parser.parse_args()
    print('Magic begins..')
    denerate_diff(Path(args.first_file).resolve(),
                  Path(args.second_file).resolve())


def denerate_diff(path_to_file1, path_to_file2):
    with open(path_to_file1) as f:
        file1 = ordered(json.load(f))
    with open(path_to_file2) as q:
        file2 = ordered(json.load(q))
    diff = difflib.Differ()
    print(type(file1))
    print(type(file2))
    result = diff.compare(file1, file2)
    # result = [line for line in result if not line.startswith(("? "))]
    removing_symbols = ['(', ')']
    print('\n'.join(result))
    return result


def my_replace(string, removing_symbols):
    result = ''.join([c for c in string if c not in removing_symbols])
    print('result in my replace', result)
    return result


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


if __name__ == '__main__':
    main()
