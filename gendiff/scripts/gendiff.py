import argparse
import json
from os import path
import yaml

from collections import defaultdict


COMMON = 'common'
CHANGED = 'changed'
ADDED = 'added'
REMOVED = 'removed'


def main():
    args = initialize_parser().parse_args()
    file1 = get_data_from_file(args.first_file)
    file2 = get_data_from_file(args.second_file)
    difference = generate_diff(file1, file2)
    print('\n'.join(render_result(difference)))


def initialize_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--f', '--format',
                        metavar='FORMAT',
                        help='set format of output')
    return parser


def generate_diff(before, after):
    difference = defaultdict(dict)
    for key in before.keys() & after.keys():
        if before[key] == after[key]:
            difference[COMMON][key] = before[key]
        else:
            difference[CHANGED][key] = [after[key], before[key]]  # noqa: E501
    for key in after.keys() - before.keys():
        difference[ADDED][key] = after[key]
    for key in before.keys() - after.keys():
        difference[REMOVED][key] = before[key]
    return difference


def get_data_from_file(path_to_file):
    file_extension = path.splitext(path_to_file)[1]
    with open(path_to_file) as f:
        if file_extension == '.json':
            file_data = json.load(f)
        else:
            file_data = yaml.load(f, Loader=yaml.FullLoader)
    return file_data


def render_result(diff_obj):
    rendered_diff = ['{']
    for diff_key in sorted(diff_obj.keys()):
        for diff_obj_key, diff_obj_value in diff_obj[diff_key].items():
            if diff_key == COMMON:
                rendered_diff.append('  {}: {}'.format(diff_obj_key,
                                                       diff_obj_value))
            elif diff_key == CHANGED:
                rendered_diff.append('- {}: {}'.format(diff_obj_key,
                                                       diff_obj_value[1]))
                rendered_diff.append('+ {}: {}'.format(diff_obj_key,
                                                       diff_obj_value[0]))
            elif diff_key == ADDED:
                rendered_diff.append('+ {}: {}'.format(diff_obj_key,
                                                       diff_obj_value))
            elif diff_key == REMOVED:
                rendered_diff.append('- {}: {}'.format(diff_obj_key,
                                                       diff_obj_value))
    rendered_diff.append('}')
    return rendered_diff


if __name__ == '__main__':
    main()
