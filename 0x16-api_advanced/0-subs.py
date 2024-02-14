#!/usr/bin/python3
"""function using reddit api"""


import requests


def number_of_subscribers(subreddit):
    """number of subs"""
    client_id = 'fsyHwM_7gSQI9-Jn3lpwOQ'
    secret_key = '1LOwBUH-z-_f8LcDIJPenc3GBdPGrQ'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    headers = {'User-Agent': 'faisalapi/0.0.1'}
    url = f'https://oauth.reddit.com/r/{subreddit}/about.json'
    resget = requests.get(url=url, auth=auth, headers=headers, allow_redirects=False)
    sub = resget.json().get('data', {}).get('subscribers')
    if resget.status_code == 200 and\
            'data' in resget.json() and 'subscribers' in resget.json()['data']:
        return (sub)
    else:
        return (0)
