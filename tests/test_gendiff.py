import os
from gendiff.scripts.gendiff import generate_diff, \
                                    render_result, \
                                    get_data_from_file
from tests.fixtures.dict_for_gendifftest import DICTIONARY_FROM_BEFORE_JSON, \
                                            DICTIONARY_FROM_AFTER_JSON, \
                                            DICTIONARY_FINAL_DIFFERENCE_JSON, \
                                            DICTIONARY_LIST_OF_DIFFERENCES_JSON


def test_render_result():
    render_result(DICTIONARY_LIST_OF_DIFFERENCES_JSON) \
                                == DICTIONARY_FINAL_DIFFERENCE_JSON


def test_generate_diff():
    assert dict(generate_diff(
                DICTIONARY_FROM_BEFORE_JSON, DICTIONARY_FROM_AFTER_JSON)) \
                                == DICTIONARY_LIST_OF_DIFFERENCES_JSON


def test_get_data_from_file():
    file_path = str(os.path.join(os.curdir, 'tests/fixtures/before.json'))
    get_data_from_file(file_path) == DICTIONARY_FROM_BEFORE_JSON
