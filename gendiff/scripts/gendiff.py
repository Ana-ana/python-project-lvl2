import argparse
import json
from os import path
import yaml
from pprint import pprint

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
    # pprint(difference)
    print('-')
    print('\n'.join(render_result(difference)))


def initialize_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--f', '--format',
                        metavar='FORMAT',
                        help='set format of output')
    return parser


# def generate_diff(before, after):
#     difference = defaultdict(dict)
#     for key in before.keys() & after.keys():
#         if before[key] == after[key]:
#             difference[COMMON][key] = before[key]
#         else:
#             difference[CHANGED][key] = [after[key], before[key]]  # noqa: E501
#     for key in after.keys() - before.keys():
#         difference[ADDED][key] = after[key]
#     for key in before.keys() - after.keys():
#         difference[REMOVED][key] = before[key]
#     return difference

def generate_diff(before, after):
    difference = defaultdict(dict)
    for key in before.keys() & after.keys():
        # print('\n common keys are {}'.format(before.keys() & after.keys()))
        # print('\n', 'key =', key, 'before[key]=', before[key], 'after[key]=', after[key])

        if isinstance(before[key], dict) and isinstance(after[key], dict):
            # print('both values are dictionaries. going deeper generate_diff()')
            difference[COMMON][key] = generate_diff(before[key], after[key])
        elif before[key] == after[key]:
            # print('elif keys & values are equal COMMON key was added')
            difference[COMMON][key] = before[key]
        else:
            # print('elif keys & values are different CHANGED key was added')
            difference[CHANGED][key] = [after[key], before[key]]

    for key in after.keys() - before.keys():
        # print('ADDED key {}'.format(key))
        difference[ADDED][key] = after[key]
    for key in before.keys() - after.keys():
        # print('REMOVED key {}'.format(key))
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


# def render_result(diff_obj):
#     rendered_diff = ['{']
#     for diff_key in sorted(diff_obj.keys()):
#         for diff_obj_key, diff_obj_value in diff_obj[diff_key].items():
#             if diff_key == COMMON:
#                 rendered_diff.append('  {}: {}'.format(diff_obj_key,
#                                                        diff_obj_value))
#             elif diff_key == CHANGED:
#                 rendered_diff.append('- {}: {}'.format(diff_obj_key,
#                                                        diff_obj_value[1]))
#                 rendered_diff.append('+ {}: {}'.format(diff_obj_key,
#                                                        diff_obj_value[0]))
#             elif diff_key == ADDED:
#                 rendered_diff.append('+ {}: {}'.format(diff_obj_key,
#                                                        diff_obj_value))
#             elif diff_key == REMOVED:
#                 rendered_diff.append('- {}: {}'.format(diff_obj_key,
#                                                        diff_obj_value))
#     rendered_diff.append('}')
#     return rendered_diff


def render_result(diff_obj):
    # print('rendering')
    # for x, y in diff_obj.items():
    #     print('{}: {}'.format(x, y))
    # print()
    rendered_diff = ['{']
    for diff_key in [COMMON, CHANGED, ADDED, REMOVED]:  #  sorted(diff_obj.keys()):
        print('-')
        print('diff_key is={} in sorted(diff_obj.keys())={}'.format(diff_key, sorted(diff_obj.keys())))

        for diff_obj_key, diff_obj_value in diff_obj[diff_key].items():
            print('diff_obj_key is={} and diff_obj_value={}'.format(diff_obj_key, diff_obj_value))
            # print('diff_obj[diff_key].items()= ', diff_obj[diff_key].items())

            if not isinstance(diff_obj_value, dict):
                if diff_key == COMMON:
                    # print('added COMMON {}: {}'.format(diff_obj_key, diff_obj_value))
                    rendered_diff.append('  {}: {}\n'.format(diff_obj_key, diff_obj_value))
                elif diff_key == CHANGED:
                    # print('added CHANGED {}: {}'.format(diff_obj_key, diff_obj_value))
                    rendered_diff.append('- {}: {}'.format(diff_obj_key, diff_obj_value[1]))
                    rendered_diff.append('+ {}: {}'.format(diff_obj_key, diff_obj_value[0]))
                elif diff_key == ADDED:
                    # print('added ADDED {}: {}'.format(diff_obj_key, diff_obj_value))
                    rendered_diff.append('+ {}: {}'.format(diff_obj_key, diff_obj_value))
                elif diff_key == REMOVED:
                    # print('added REMOVED {}: {}'.format(diff_obj_key, diff_obj_value))
                    rendered_diff.append('- {}: {}'.format(diff_obj_key, diff_obj_value))

            elif diff_obj_key not in diff_obj:
                continue
            elif isinstance(diff_obj_value, dict):
                print('Going deeper. render_result {}'.format(diff_obj_value))
                rendered_diff.append('{}: {}'.format(diff_obj_key, render_result({COMMON: diff_obj_value})))
    rendered_diff.append('}')
    return rendered_diff


if __name__ == '__main__':
    main()
