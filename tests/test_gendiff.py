import os

import pytest

from gendiff.scripts.gendiff import generate_diff, \
                                    render_diff, \
                                    get_data_from_file

from tests.fixtures.data_gendifftest import (
                                               rendered_difference,
                                               difference,
                                               content_before,
                                               content_after,
                                            )


@pytest.mark.skip(reason='will be changed in next itteration')
def test_render_result(rendered_difference, difference):
    assert render_diff(difference) == rendered_difference


@pytest.mark.skip(reason='generate_diff() will be changed in next itteration')
def test_generate_diff(content_before, content_after, difference):
    assert generate_diff(content_before, content_after) == difference


@pytest.mark.parametrize("input_path", ['tests/fixtures/before.json', 'tests/fixtures/before.yaml'])
def test_get_data_from_file(content_before, input_path):
    file_path = str(os.path.join(os.curdir, input_path))
    assert get_data_from_file(file_path) == content_before

