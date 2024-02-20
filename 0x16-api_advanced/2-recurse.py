#!/usr/bin/python3
"""using reddit api"""


import requests
after = None


def recurse(subreddit, hot_list=[]):
    """recursive function returns list containing title of all hot articles"""
    client_id = 'fsyHwM_7gSQI9-Jn3lpwOQ'
    secret_key = '1LOwBUH-z-_f8LcDIJPenc3GBdPGrQ'
    global after
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
        after = data['after']
        if after is not None:
            after = data['after']
            recurse(subreddit, hot_list)
        for item in listofitems:
            hot_list.append(item['data']['title'])
        return (hot_list)
    else:
        return (None)

