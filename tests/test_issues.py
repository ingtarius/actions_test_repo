import json

import pytest
import requests
import requests_mock

from src.issues import *


@pytest.fixture
def mock_get():
    with requests_mock.Mocker() as requests_mocker:
        requests_mocker.get(
            "https://mock-test.example.com/test_url/issues",
            status_code=200,
            json={"the_result": "was successful!"},
        )
        yield


def test_get_data(mock_get):
    get_data('https://mock-test.example.com/test_url/issues')

