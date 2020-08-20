import pytest



DICTIONARY_FROM_AFTER = {"timeout": 20,
                         "verbose": True,
                         "host": "hexlet.io"}

DICTIONARY_FINAL_DIFFERENCE = {'  host': 'hexlet.io',
                               '- timeout': 50,
                               '+ timeout': 20,
                               '+ verbose': True,
                               '- proxy': '123.234.53.22'}




@pytest.fixture
def content_before():
    return {"host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22"}


@pytest.fixture()
def content_after():
    return {"timeout": 20,
            "verbose": True,
            "host": "hexlet.io"}


@pytest.fixture()
def rendered_difference():
    return '{\n' \
           '  host: hexlet.io\n' \
           '- timeout: 50\n'\
           '+ timeout: 20\n' \
           '+ verbose: True\n' \
           '- proxy: 123.234.53.22\n' \
           '}'


# {'  host': 'hexlet.io',
#             '- timeout': 50,
#             '+ timeout': 20,
#             '+ verbose': True,
#             '- proxy': '123.234.53.22'}


@pytest.fixture()
def difference():
    return {'common': {'host': 'hexlet.io'},
            'changed': {'timeout': [20, 50]},
            'added': {'verbose': True},
            'removed': {'proxy': '123.234.53.22'}}
