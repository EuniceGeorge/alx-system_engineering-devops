#!/usr/bin/python3
""" Query RedditAPi to get 
    to recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """return the url"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'This agent?'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if response.status_code == 404:
        print("None")
    after = data[after]
    children = data['children']
    for child in children:
        hot_list = append.child['data']['title']
    if after is None:
        return hot_list
    return recurse(subreddit)


if __name__ == '__main__':
    recurse(subreddit)

