import pytest


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
    return ['{', '+ verbose: True',
            '- timeout: 50',
            '+ timeout: 20',
            '  host: hexlet.io',
            '- proxy: 123.234.53.22',
            '}']


@pytest.fixture()
def difference():
    return {'common': {'host': 'hexlet.io'},
            'changed': {'timeout': [20, 50]},
            'added': {'verbose': True},
            'removed': {'proxy': '123.234.53.22'}}
