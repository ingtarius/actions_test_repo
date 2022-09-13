import requests


def test_get_all_repos_org(requests_mock):
    requests_mock.get('https://api.github.com', text='test')
    print(requests.get('https://api.github.com').text)
    assert 'test' == requests.get('https://api.github.com').text


def test_get_issues_from_url(requests_mock):
    requests_mock.get('https://api.github.com', text='test')
    print(requests.get('https://api.github.com').text)
    assert 'test' == requests.get('https://api.github.com').text
