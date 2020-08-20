import argparse
import json

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
    file1 = get_data_from_file_json(args.first_file)
    file2 = get_data_from_file_json(args.second_file)
    difference = generate_diff(file1, file2)
    print(render_result(difference))


def generate_diff(before, after):
    difference = defaultdict(dict)
    for item in [COMMON, CHANGED, ADDED, REMOVED]:
        difference[item]
    for key in before.keys() & after.keys():
        if before[key] == after[key]:
            difference[COMMON][key] = before[key]
        else:
            difference[CHANGED][key] = [after[key], before[key]]  # noqa: E501
    for key in set(after.keys()) - set(before.keys()):
        difference[ADDED][key] = after[key]
    for key in set(before.keys()) - set(after.keys()):
        difference[REMOVED][key] = before[key]
    return difference


def get_data_from_file_json(path_to_file):
    with open(path_to_file) as f:
        file_data = json.load(f)
    return file_data


def get_data_from_file_yaml(path_to_file):
    file_data = 2
    return file_data


def render_result(diff_obj):
    rendered_diff = defaultdict(dict)
    for diff_key in [COMMON, CHANGED, ADDED, REMOVED]:
        for diff_obj_key, diff_obj_value in diff_obj[diff_key].items():
            if diff_key == COMMON:
                rendered_diff['  ' + diff_obj_key] = diff_obj_value
            elif diff_key == CHANGED:
                rendered_diff['- ' + diff_obj_key] = diff_obj_value[1]
                rendered_diff['+ ' + diff_obj_key] = diff_obj_value[0]
            elif diff_key == ADDED:
                rendered_diff['+ ' + diff_obj_key] = diff_obj_value
            elif diff_key == REMOVED:
                rendered_diff['- ' + diff_obj_key] = diff_obj_value
    render_pretty_output = '{'
    for x, y in rendered_diff.items():
        render_pretty_output = render_pretty_output + '\n'
        render_pretty_output = render_pretty_output + ''\
            .join('{}: {}'.format(x, y))
    render_pretty_output = render_pretty_output + '\n' + '}'

    # print('render')
    # # print('\n'.join(rendered_diff))
    # print(render_pretty_output)
    # print()
    return render_pretty_output


if __name__ == '__main__':
    main()
