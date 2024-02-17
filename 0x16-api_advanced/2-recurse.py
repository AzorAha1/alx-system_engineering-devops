#!/usr/bin/python3
"""using reddit api"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive function returns list containing title of all hot articles"""
    client_id = 'fsyHwM_7gSQI9-Jn3lpwOQ'
    secret_key = '1LOwBUH-z-_f8LcDIJPenc3GBdPGrQ'
    params = {
        'after': after
    }
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    headers = {'User-Agent': 'faisalapi/0.0.1'}
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json'
    resget = requests.get(auth=auth, headers=headers, url=url, params=params)
    if resget.status_code == 200:
        data = resget.json()['data']
        listofitems = data['children']
        for item in listofitems:
            hot_list.append(item['data']['title'])
        after = data['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)

