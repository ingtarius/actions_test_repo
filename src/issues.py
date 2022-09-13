#!/usr/bin/env python

import requests
import sys

# Vars
ORG = 'devopshq'
# Testing only, skip limit
#token = ''
#headers = {'Authorization': 'token ' + token}
GIT_API_URL = 'https://api.github.com'


def get_all_repos_org(org):
    """ Get all repos from specific org in github """
    """ https://docs.github.com/en/rest/repos/repos#list-organization-repositories """
    full_url = GIT_API_URL + '/orgs/' + org + '/repos'
    r = requests.get(full_url)
    if r.status_code != 200:
        print("Failed. Responce code is %s while get all repos!" % (r.status_code))
        sys.exit()
    else:
        return r.json()


def get_issues_from_url(url):
    """ Get all issues from github url """
    """ https://docs.github.com/en/rest/issues/issues#list-repository-issues """
    full_url = url + '/issues'
    r = requests.get(full_url)
    if r.status_code != 200:
        print("Failed. Responce code is %s while get issue from repo!" % (r.status_code))
        sys.exit()
    else:
        return r.json()


for repo in get_all_repos_org(ORG):
    print("%s:" % (repo['name']))
    for issue in get_issues_from_url(repo['url']):
        print('#%s %s' % (issue['number'], issue['title']))
