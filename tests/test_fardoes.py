import os

import fardoes
import pytest


@pytest.fixture
def test_data_dir():
    return os.path.join(os.path.dirname(__file__), "test_data")


def test_parse_log(test_data_dir):
    log_file = os.path.join(test_data_dir, "log.txt")
    with open(log_file, "r") as file:
        log = file.read()
    containers, times = fardoes.parse_log(log)
    assert list(containers) == [1, 2, 4]
    assert list(times) == [448.372, 554.845, 767.752]


def test_parse_empty_log():
    log = ""
    containers, times = fardoes.parse_log(log)
    assert list(containers) == []
    assert list(times) == []
