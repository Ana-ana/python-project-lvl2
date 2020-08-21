import os

import pytest

from gendiff.scripts.gendiff import generate_diff, \
                                    render_result, \
                                    get_data_from_file_json, \
                                    get_data_from_file_yaml
from tests.fixtures.dict_for_gendifftest import (
                                               rendered_difference,
                                               difference,
                                               content_before,
                                               content_after,
                                            )


def test_render_result(rendered_difference, difference):
    assert render_result(difference) == rendered_difference


def test_generate_diff(content_before, content_after, difference):
    assert generate_diff(content_before, content_after) == difference


def test_get_data_from_file_json(content_before):
    file_path = str(os.path.join(os.curdir, 'tests/fixtures/before.json'))
    assert get_data_from_file_json(file_path) == content_before


@pytest.mark.skip('not ready')
def test_get_data_from_file_yaml(content_before):
    file_path = str(os.path.join(os.curdir, 'tests/fixtures/before.yaml'))
    assert get_data_from_file_yaml(file_path) == content_before
