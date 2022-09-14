#!/usr/bin/env python

import requests
import sys

# Vars
ORG = 'devopshq'
# Testing only, skip limit
# token = ''
# headers = {'Authorization': 'token ' + token}
GIT_API_URL = 'https://api.github.com'


def get_data(url):
    """ Collect data from remote api """
    """ https://docs.github.com/en/rest/repos/repos#list-organization-repositories """
    """ https://docs.github.com/en/rest/issues/issues#list-repository-issues """
    r = requests.get(url)
    if r.status_code != 200:
        print("Failed. Responce code is %s while get url %s!" % (r.status_code, url))
        sys.exit()
    else:
        return r.json()


if __name__ == "__main__":
    repos_list_url = GIT_API_URL + '/orgs/' + ORG + '/repos'
    for repo in get_data(repos_list_url):
        print("%s:" % (repo['name']))
        issue_url = repo['url'] + '/issues'
        for issue in get_data(issue_url):
            print('#%s %s' % (issue['number'], issue['title']))
