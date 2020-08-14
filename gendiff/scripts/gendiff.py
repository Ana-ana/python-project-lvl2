import argparse
import json
import  os
from pathlib import Path
from pprint import pprint, pformat
from collections import defaultdict

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('--f', '--format',
                    metavar='FORMAT',
                    help='set format of output')


def main():
    args = parser.parse_args()
    generate_diff(
                            get_data_from_file(Path(args.first_file).resolve()),
                            get_data_from_file(Path(args.second_file).resolve()))


def generate_diff(file_data1, file_data2):
    keys = ['common ', 'changed ', 'added ', 'removed ']
    difference = defaultdict(dict)
    for item in keys:
        difference[item]

    # for x, y in difference.items():
    #     print('{} :{}'.format(x, y))
    # print()

    for key in set(file_data1.keys()) & set(file_data2.keys()):
        if file_data1[key] == file_data2[key]:
           difference['common '][key] = file_data1[key]
           for x, y in difference.items():
        else:
            difference['changed '][key] = [file_data2[key],
                                           file_data1[key]]
    for key in set(file_data2.keys()) - set(file_data1.keys()):
        difference['added '][key] = file_data2[key]
    for key in set(file_data1.keys()) - set(file_data2.keys()):
        difference['removed '][key] = file_data1[key]

    print(type(difference), 'difference')
    for x, y in difference.items():
        print('{} :{}'.format(x, y))
    return difference


def get_data_from_file(path_to_file):
    with open(path_to_file) as f:
        file_data = json.load(f)
    return file_data

def check_path(path_to_file):
    if os.path.isfile(path_to_file):
        print('is file', path_to_file)
        return path_to_file
    else:
        print(os.path.abspath(path_to_file))
        return os.path.abspath(path_to_file)

def print_result(result_obj):
    for x, y in result_obj.items():
        print('{} :{}'.format(x, y))

# diff = {
#     'same': {'host': 'hexlet.io'},
#     'changed': {'timeout': [50, 20]},
#     'added': {'verbose: True'},
#     'removed': {},
# }





def find_sum(a, b):
    return a + b


if __name__ == '__main__':
    main()

