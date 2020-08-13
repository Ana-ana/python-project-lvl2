import argparse
import json
import  os
from pathlib import Path

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('--f', '--format',
                    metavar='FORMAT',
                    help='set format of output')


def main():
    args = parser.parse_args()
    generate_diff(get_data_from_file(Path(args.first_file).resolve()),
                  get_data_from_file(Path(args.second_file).resolve()))


def generate_diff(file_data1, file_data2):
    keys = ['  ', '+ ', '- ']
    # difference = dict.fromkeys(['  ', '+ ', '- '])
    difference = {}
    for _ in keys:
        difference.setdefault(_, [])
    for key in set(file_data1.keys()) & set(file_data2.keys()):
        if file_data1[key] == file_data2[key]:
            difference['  '].append({key: file_data1[key]})
        else:
            difference['+ '].append({key: file_data2[key]})
            difference['- '].append({key: file_data1[key]})
    for key in set(file_data2.keys()) - set(file_data1.keys()):
        difference['+ '].append({key: file_data2[key]})
    # for key in set(file_data1.keys()) - set(file_data2.keys()):
    #     difference['- ' + key] = file_data1[key]

    print('difference')
    for x, y in difference.items():
        print('{} :{}'.format(x, y))


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




def find_sum(a, b):
    return a + b


if __name__ == '__main__':
    main()

