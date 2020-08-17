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

KEYS = ['common', 'changed', 'added', 'removed']


def main():
    args = parser.parse_args()
    print('\n'.join(render_result(generate_diff(
        get_data_from_file(args.first_file),
        get_data_from_file(args.second_file)))))


def generate_diff(file_data1, file_data2):
    difference = defaultdict(dict)
    for item in KEYS:
        difference[item]
    for key in set(file_data1.keys()) & set(file_data2.keys()):
        if file_data1[key] == file_data2[key]:
            difference['common'][key] = file_data1[key]
        else:
            difference['changed'][key] = [file_data2[key],
                                          file_data1[key]]
    for key in set(file_data2.keys()) - set(file_data1.keys()):
        difference['added'][key] = file_data2[key]
    for key in set(file_data1.keys()) - set(file_data2.keys()):
        difference['removed'][key] = file_data1[key]
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


def render_result(result_obj):
    rendered_result = ['{']
    for key_of_change, params in result_obj.items():
        for file_key, file_key_value in params.items():
            if key_of_change == 'common':
                rendered_result.append('  {}: {}'
                                       .format(file_key, file_key_value))
            elif key_of_change == 'changed':
                rendered_result.append('- {}: {}'
                                       .format(file_key, file_key_value[1]))
                rendered_result.append('+ {}: {}'
                                       .format(file_key, file_key_value[0]))
            elif key_of_change == 'added':
                rendered_result.append('+ {}: {}'
                                       .format(file_key, file_key_value))
            elif key_of_change == 'removed':
                rendered_result.append('- {}: {}'
                                       .format(file_key, file_key_value))
    rendered_result.append('}')
    return rendered_result


if __name__ == '__main__':
    main()
