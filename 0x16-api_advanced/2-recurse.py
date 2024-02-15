#!/usr/bin/python3
"""using reddit api"""


import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """recursive function returns list containing title of all hot articles"""
    client_id = 'fsyHwM_7gSQI9-Jn3lpwOQ'
    secret_key = '1LOwBUH-z-_f8LcDIJPenc3GBdPGrQ'
    subreddit = sys.argv[1]
    params = {
        't': 'day',
        'after': after
    }
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    headers = {'User-Agent': 'faisalapi/0.0.1'}
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json'
    resget = requests.get(auth=auth, headers=headers, url=url, params=params)
    if resget.status_code == 200:
        previous = resget.json()['data']['after']
        listofitems = resget.json()['data']['children']
        for item in listofitems:
            hot_list.append(item['data']['title'])
        if previous is not None:
            recurse(subreddit=subreddit, hot_list=hot_list, after=previous)
        return hot_list
    else:
        return None
