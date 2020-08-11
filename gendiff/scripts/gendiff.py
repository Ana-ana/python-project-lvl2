import argparse
import json
import difflib
from pathlib import Path

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('--f', '--format',
                    metavar='FORMAT',
                    help='set format of output')


def main():
    args = parser.parse_args()
    print('Magic begins..')
    denerate_diff(Path(args.first_file).resolve(),
                  Path(args.second_file).resolve())


def denerate_diff(path_to_file1, path_to_file2):
    with open(path_to_file1) as f:
        file1 = f.readlines()  # json.load(f)
    with open(path_to_file2) as q:
        file2 = q.readlines() #json.load(q)
    # print(file1)
    # print()
    # print(file2)
    diff = difflib.Differ()
    result = diff.compare(file1, file2)
    result = [line for line in result if line.startswith(("- ", "+ ", " "))]
    # print(type(result))
    print(''.join(list(result)))
    # print(list(result))
    return result

    # for key, value in file1.items():
    #     for k, v in file2.items():
    #         if key in file2.keys():
    #             if file1.get(key) == file2.get(k):
    #                 print('Common key: value')
    #                 print('file1.get(key) {} == file2.get(k) {}'.format(file1.get(key),
    #                                                                     file2.get(k)))
    #                 print('key file1 {} and key file2 {}'.format(key, k))
    #             else:
    #                 print()
    #                 print('else works')
    #                 print('Value been changed')
    #                 print('file1.get(key) {} == file2.get(k) {}'.format(file1.get(key),
    #                                                                     file2.get(k)))
    #                 print('key file1 {} and key file2 {}'.format(key, k))
    #
    # d = {x: file1[x] for x in file1 if x in file2}
    # print(d)


if __name__ == '__main__':
    main()
