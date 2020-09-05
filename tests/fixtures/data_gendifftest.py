import pytest


COMMON = 'common'
CHANGED = 'changed'
ADDED = 'added'
REMOVED = 'removed'
NESTED = 'nested'


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
    str = 'some random string'
    # need to add data for tests
    return str


@pytest.fixture()
def difference():
    return ['{', '+ verbose: True',
            '- timeout: 50',
            '+ timeout: 20',
            '  host: hexlet.io',
            '- proxy: 123.234.53.22',
            '}']
    # return {
    # NESTED: {
    #     'commmmmon': {
    #         COMMON: {
    #             'key2': 'value1',
    #         },
    #         ADDED: {
    #             'key3': 'value2',
    #         },
    #         CHANGED: {
    #             'baz': [1, 5],
    #             'kkkeey': [True, {'key': 'value12'}],
    #             'new_key': [{'key11': 'value11'}, 'new_strine']
    #         },
    #     }
    # },
    # ADDED: {
    #     'key4': {
    #         'key5': {
    #             'key6': 'value3',
    #         }
    #     }
    # },
    # REMOVED: {
    #     'foo': 'bar',
    # }
    # }
