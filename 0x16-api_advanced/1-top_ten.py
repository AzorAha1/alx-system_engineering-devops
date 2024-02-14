#!/usr/bin/python3
"""function using reddit api"""


import requests


def top_ten(subreddit):
    """top ten posts in a subreddit"""
    client_id = 'fsyHwM_7gSQI9-Jn3lpwOQ'
    secret_key = '1LOwBUH-z-_f8LcDIJPenc3GBdPGrQ'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    headers = {'User-Agent': 'faisalapi/0.0.1'}
    url = f'https://oauth.reddit.com/r/{subreddit}/top.json?t=day&limit=10'
    resget = requests.get(url=url, auth=auth, headers=headers)
    if resget.status_code == 200:
        subs = resget.json().get('data', {}).get('children')
        for sub in subs:
            print(sub.get('data', {}).get('title'))
    else:
        print(None)
