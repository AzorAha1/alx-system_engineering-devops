#!/usr/bin/python3
"""using reddit api"""


import requests


def recurse(subreddit, hot_list=[]):
    """recursive function returns list containing title of all hot articles"""
    client_id = 'fsyHwM_7gSQI9-Jn3lpwOQ'
    secret_key = '1LOwBUH-z-_f8LcDIJPenc3GBdPGrQ'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    headers = {'User-Agent': 'faisalapi/0.0.1'}
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json?t=day'
    resget = requests.get(auth=auth, headers=headers, url=url)
    print(resget.json())
