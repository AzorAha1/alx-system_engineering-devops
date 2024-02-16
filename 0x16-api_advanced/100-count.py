#!/usr/bin/python3
"""using reddit api"""


import requests


def count_words(subreddit, word_list=[], after=None):
    """recursive function returns list containing title of all hot articles and count of keywords"""
    client_id = 'fsyHwM_7gSQI9-Jn3lpwOQ'
    secret_key = '1LOwBUH-z-_f8LcDIJPenc3GBdPGrQ'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    headers = {'User-Agent': 'faisalapi/0.0.1'}
    params = {
        'after': after
    }
    url = f'https://oauth.reddit.com/r/{subreddit}/hot.json'
    resget = requests.get(auth=auth, headers=headers,
                        url=url, params=params, allow_redirects=False)
    if resget.status_code == 200:
        data = resget.json()['data']
        listofitems = data['children']
        for item in listofitems:
            word_list.append(item['data']['title'])
        after = data['after']
        if after is not None:
            count_words(subreddit=subreddit, word_list=word_list, after=after)
        print(f'{word_list[item]}: {len(word_list)}')
    else:
        return None

