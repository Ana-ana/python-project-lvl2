import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    parser.parse_args()
    print('Hello')


if __name__ == '__main__':
    main()
