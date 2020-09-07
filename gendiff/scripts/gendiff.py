import argparse
import json
from os import path
import yaml
import pprint

from collections import defaultdict


COMMON = 'common'
CHANGED = 'changed'
ADDED = 'added'
REMOVED = 'removed'
NESTED = 'nested'

INDENT = {
    'added': '+ ',
    'removed': '- ',
    'common': '  ',
    'changed': '',
    'nested': ''
}


def main():
    args = initialize_parser().parse_args()
    file1 = get_data_from_file(args.first_file)
    file2 = get_data_from_file(args.second_file)
    difference = generate_diff(file1, file2)
    if args.f == 'plain':
        for item in render_plain(difference):
            print('Property ' + item)
    else:
        print(''.join(render_diff(difference)))


def initialize_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument('--f', '--format',
                        metavar='FORMAT',
                        help='set format of output')
    return parser


def generate_diff(before, after):
    difference = defaultdict(dict)
    for key in before.keys() & after.keys():
        if isinstance(before[key], dict) and isinstance(after[key], dict):
            difference[NESTED][key] = generate_diff(before[key], after[key])
        elif before[key] == after[key]:
            difference[COMMON][key] = before[key]
        else:
            difference[CHANGED][key] = [after[key], before[key]]
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


def render_diff(diff_obj, indent=' '):
    rendered_diff = ['{']
    for diff_key in sorted(diff_obj.keys()):
        for diff_obj_key, diff_obj_value in diff_obj[diff_key].items():
            if diff_key == NESTED:
                rendered_diff.append(
                    format_output(INDENT[diff_key], diff_obj_key, render_diff(diff_obj_value, indent + ' ' * 2), indent))  # noqa: E501
            elif isinstance(diff_obj_value, dict):
                rendered_diff.append(format_output(
                    INDENT[diff_key], diff_obj_key, render_diff({COMMON: diff_obj_value}, indent + ' ' * 2), indent))  # noqa: E501
            else:
                if diff_key == COMMON:
                    rendered_diff.append(format_output(INDENT[COMMON], diff_obj_key, diff_obj_value, indent))  # noqa: E501
                elif diff_key == CHANGED:
                    rendered_diff.append(format_output(INDENT[REMOVED], diff_obj_key, diff_obj_value[1], indent))  # noqa: E501
                    rendered_diff.append(format_output(INDENT[ADDED], diff_obj_key, diff_obj_value[0], indent))  # noqa: E501
                elif diff_key == ADDED:
                    rendered_diff.append(format_output(INDENT[ADDED], diff_obj_key, diff_obj_value, indent))  # noqa: E501
                elif diff_key == REMOVED:
                    rendered_diff.append(format_output(INDENT[REMOVED], diff_obj_key, diff_obj_value, indent))  # noqa: E501
    rendered_diff.append(indent + '}')
    return '\n'.join(rendered_diff)


def render_plain(diff_obj):
    rendered_str = []
    for diff_key in sorted(diff_obj.keys()):
        for k, v in diff_obj[diff_key].items():
            if diff_key == NESTED:
                for _ in render_plain(v):
                    rendered_str.append('{}.{}'.format(k, _))
            else:
                if diff_key == ADDED:
                    rendered_str.append('{} was added with value {}'.format(k, replace_dict(v)))
                if diff_key == REMOVED:
                    rendered_str.append('{} was removed'.format(k))
                if diff_key == CHANGED:
                    rendered_str.append('{} was updated from {} to {}.'.format(k, replace_dict(v[1]), replace_dict(v[0])))
    return rendered_str

def replace_dict(itm):
    if isinstance(itm, dict):
        itm = '[complex value]'
    return itm




def format_output(action_key, dic_key, dic_value, indent):
    if isinstance(dic_value, dict):
        rendered_dict = ['{']
        for key, value in dic_value.items():
            rendered_dict.append('{}{}: {}'.format(indent * 4, key, value))
        rendered_dict.append(indent * 2 + '}')
        return '{}{}{}: {}'.format(indent, action_key, dic_key, '\n'.join(rendered_dict))  # noqa: E501
    else:
        return '{}{}{}: {}'.format(indent, action_key, dic_key, dic_value)


if __name__ == '__main__':
    main()
