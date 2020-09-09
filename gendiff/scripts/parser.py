import argparse
import json
from os import path

import yaml


def initialize_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument('--f', '--format', nargs='?', default='json',
                        metavar='FORMAT',
                        help='set format of output')
    return parser


def get_data_from_file(path_to_file):
    file_extension = path.splitext(path_to_file)[1]
    with open(path_to_file) as f:
        if file_extension == '.json':
            file_data = json.load(f)
        else:
            file_data = yaml.load(f, Loader=yaml.FullLoader)
    return file_data
