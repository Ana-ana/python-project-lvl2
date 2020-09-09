from gendiff.scripts.parser import initialize_parser, \
                                    get_data_from_file
from gendiff.scripts.render_json import render_json
from gendiff.scripts.render_plain import render_plain
from gendiff.scripts.generate_difference import *


def main():
    args = initialize_parser().parse_args()
    file1 = get_data_from_file(args.first_file)
    file2 = get_data_from_file(args.second_file)
    difference = generate_diff(file1, file2)
    if args.f == 'json':
        print(''.join(render_json(difference)))
    if args.f == 'plain':
        print('\n'.join(render_plain(difference)))


if __name__ == '__main__':
    main()
