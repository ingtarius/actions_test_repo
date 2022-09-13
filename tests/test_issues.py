import json

import pytest
import requests
import requests_mock

from src.issues import *

@pytest.fixture
def mock_get_org():
    with requests_mock.Mocker() as requests_mocker:
        requests_mocker.get(
            "https://api.github.com/orgs/test_org/repos",
            status_code=200,
            json={"the_result": "was successful!"},  # Optional. The value when .json() is called on the response.
        )
        yield


@pytest.fixture
def mock_get_issue():
    with requests_mock.Mocker() as requests_mocker:
        requests_mocker.get(
            "https://mock-test.example.com/test_url/issues",
            status_code=200,
            json={"the_result": "was successful!"},  # Optional. The value when .json() is called on the response.
        )
        yield



def test_get_all_repos_org(mock_get_org):
    get_all_repos_org('test_org')

def test_get_issues_from_url(mock_get_issue):
    get_issues_from_url('https://mock-test.example.com/test_url')
