import pathlib

import fardoes
import pytest


@pytest.fixture
def test_data_dir():
    return pathlib.Path(__file__).parent / "test_data"


def test_parse_log(test_data_dir):
    log_file = test_data_dir / "log.txt"
    with log_file.open("r") as file:
        log = file.read()
    containers, times = fardoes.parse_log(log)
    assert list(containers) == [1, 2, 4]
    assert list(times) == [448.372, 554.845, 767.752]


def test_parse_empty_log():
    log = ""
    containers, times = fardoes.parse_log(log)
    assert list(containers) == []
    assert list(times) == []
