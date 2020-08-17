from gendiff.scripts.gendiff import generate_diff, \
                                    render_result, \
                                    get_data_from_file


def test_render_result():
    to_be_rendered = {'common ': {'host': 'hexlet.io'},
                    'changed ': {'timeout': [20, 50]},
                    'added ': {'verbose': True},
                    'removed ': {'proxy': '123.234.53.22'}}
    expected_result = {'  host': 'hexlet.io',
                       '- timeout': 50,
                       '+ timeout': 20,
                       '+ verbose': True,
                       '- proxy': '123.234.53.22'}
    render_result(to_be_rendered) == expected_result


def test_generate_diff():
    before_dict = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22"}
    after_dict = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    expected_res = {'common': {'host': 'hexlet.io'},
                    'changed': {'timeout': [20, 50]},
                    'added': {'verbose': True},
                    'removed': {'proxy': '123.234.53.22'}}
    assert generate_diff(before_dict, after_dict) == expected_res


def test_get_data_from_file():
    expected_result = {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22"}
    file_path = '/home/user/python-project-lvl2/gendiff/scripts/before.json'
    get_data_from_file(file_path) == expected_result
