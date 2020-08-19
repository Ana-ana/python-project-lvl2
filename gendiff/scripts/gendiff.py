import argparse
import json
import os

from collections import defaultdict

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('--f', '--format',
                    metavar='FORMAT',
                    help='set format of output')


COMMON = 'common'
CHANGED = 'changed'
ADDED = 'added'
REMOVED = 'removed'


def main():
    args = parser.parse_args()
    print('{')
    for k, v in render_result(generate_diff(
                                get_data_from_file_json(args.first_file),
                                get_data_from_file_json(args.second_file)))\
            .items():
        print('{}: {}'.format(k, v))
    print('}')


def generate_diff(file_data1, file_data2):
    difference = defaultdict(dict)
    for item in [COMMON, CHANGED, ADDED, REMOVED]:
        difference[item]
    for key in set(file_data1.keys()) & set(file_data2.keys()):
        if file_data1[key] == file_data2[key]:
            difference[COMMON][key] = file_data1[key]
        else:
            difference[CHANGED][key] = [file_data2[key],
                                        file_data1[key]]
    for key in set(file_data2.keys()) - set(file_data1.keys()):
        difference[ADDED][key] = file_data2[key]
    for key in set(file_data1.keys()) - set(file_data2.keys()):
        difference[REMOVED][key] = file_data1[key]
    return difference


def get_data_from_file_json(path_to_file):
    with open(path_to_file) as f:
        file_data = json.load(f)
    return file_data


def get_data_from_file_yaml(path_to_file):
    file_data = 2
    return file_data


def check_path(path_to_file):
    if os.path.isfile(path_to_file):
        print('is file', path_to_file)
        return path_to_file
    else:
        print(os.path.abspath(path_to_file))
        return os.path.abspath(path_to_file)
#  tried to right function to check path to file.


def render_result(result_obj):
    rendered_result = defaultdict(dict)
    for key_of_change, params in result_obj.items():
        for file_key, file_key_value in params.items():
            if key_of_change == COMMON:
                rendered_result['  ' + file_key] = file_key_value
            elif key_of_change == CHANGED:
                rendered_result['- ' + file_key] = file_key_value[1]
                rendered_result['+ ' + file_key] = file_key_value[0]
            elif key_of_change == ADDED:
                rendered_result['+ ' + file_key] = file_key_value
            elif key_of_change == REMOVED:
                rendered_result['- ' + file_key] = file_key_value
    return rendered_result


if __name__ == '__main__':
    main()
