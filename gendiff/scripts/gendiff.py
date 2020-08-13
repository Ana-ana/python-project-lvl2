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
    generate_diff(Path(args.first_file).resolve(),
                  Path(args.second_file).resolve())


def generate_diff(path_to_file1, path_to_file2):
    file_data1 = get_data_from_file(path_to_file1)
    file_data2 = get_data_from_file(path_to_file2)
    print('{')
    for key, value in file_data1.items():
        if key in file_data2.keys():
            if value == file_data2[key]:
                print('  {}:{}'.format(key, value))
            else:
                print('+ {}: {}'.format(key, file_data2[key]))
                print('- {}: {}'.format(key, file_data1[key]))
        if key not in file_data2.keys():
            print('- {}: {}'.format(key, file_data1[key]))
    for key, value in file_data2.items():
        if key not in file_data1.keys():
            print('+ {}: {}'.format(key, file_data2[key]))
    print('}')


def get_data_from_file(path_to_file):
    with open(path_to_file) as f:
        file_data = json.load(f)
    return file_data


if __name__ == '__main__':
    main()
