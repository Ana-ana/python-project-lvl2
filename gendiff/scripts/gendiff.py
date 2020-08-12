import argparse
import json
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
        file1 = json.load(f)
    with open(path_to_file2) as q:
        file2 = json.load(q)
    for (key, value) in set(file1.items()) & set(file2.items()):
        print('   {}: {} in both'.format(key, value))
    for (key, value) in set(file2.items()) - set(file1.items()):
        print('+  {}: {} was added'.format(key, value))
    for (key, value) in set(file1.items()) - set(file2.items()):
        print('-  {}: {} was deleted'.format(key, value))


if __name__ == '__main__':
    main()
