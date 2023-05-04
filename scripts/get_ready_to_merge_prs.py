#! /usr/bin/env python3

"""
Command-line script to get open prs of both organizations with label 'Ready to merge'
"""
import json
import logging
import os
import sys

import requests


LOG = logging.getLogger(__file__)

GIT_API_URL = 'https://api.github.com/search/issues?per_page=100'
ORGS = ['edx', 'openedx']


def get_ready_to_merge_prs(org: str):
    """
    get a list of all prs which are open and have a label "Ready to merge" in organization.

    Args:
        org (str):
        token (str):

    Returns:
            list of all prs.
    """
    token = os.environ.get('GIT_TOKEN')
    if not token:
        LOG.error('GIT_TOKEN is missing from environment variables')
        sys.exit(1)
    urls = get_github_api_response(org, token)
    print(json.dumps(urls))
    return urls


def get_github_api_response(org, token):
    """
    get github pull requests
    https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests
    """
    params = f'q=is:pr is:open label:"Ready to merge" org:{org}'
    headers = {
        'Accept': "application/vnd.github.antiope-preview+json",
        'Authorization': "bearer {token}".format(token=token),
    }
    data = []

    try:
        resp = requests.get(GIT_API_URL, params=params, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            data = [item['html_url'] for item in data['items']]
        else:
            LOG.error(
                'api return status code {code} and error {con}'.format(code=resp.status_code, con=resp.content)
            )
            sys.exit(1)

    except Exception as err:
        LOG.error('Github api throws error: {con}'.format(con=str(err)))
        sys.exit(1)

    return data


def parse_urls(data):
    """
    parse data to return only org, repo and pull request number
    """
    raw_data = data.replace('https://github.com/', '').split('/')
    return raw_data[0], raw_data[1], raw_data[3]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_ready_to_merge_prs(sys.argv[1])
    else:
        print(f"Please provide a valid github org name.  {', '.join(ORGS)} are examples of valid organizations.")
