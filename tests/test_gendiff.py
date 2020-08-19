import os

import pytest

from gendiff.scripts.gendiff import generate_diff, \
                                    render_result, \
                                    get_data_from_file_json, \
                                    get_data_from_file_yaml

from tests.fixtures.dict_for_gendifftest import DICTIONARY_FROM_BEFORE, \
                                            DICTIONARY_FROM_AFTER, \
                                            DICTIONARY_FINAL_DIFFERENCE, \
                                            DICTIONARY_LIST_OF_DIFFERENCES


def test_render_result():
    assert render_result(DICTIONARY_LIST_OF_DIFFERENCES) \
                            == DICTIONARY_FINAL_DIFFERENCE


def test_generate_diff():
    assert dict(generate_diff(
                DICTIONARY_FROM_BEFORE, DICTIONARY_FROM_AFTER)) \
           == DICTIONARY_LIST_OF_DIFFERENCES


def test_get_data_from_file_json():
    file_path = str(os.path.join(os.curdir, 'tests/fixtures/before.json'))
    assert get_data_from_file_json(file_path) == DICTIONARY_FROM_BEFORE


@pytest.mark.skip('not ready')
def test_get_data_from_file_yaml():
    file_path = str(os.path.join(os.curdir, 'tests/fixtures/before.yaml'))
    assert get_data_from_file_yaml(file_path) == DICTIONARY_FROM_BEFORE
