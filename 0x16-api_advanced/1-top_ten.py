#!/usr/bin/python3
""" Query RedditAPi to get
    the first 10 titles
"""

import requests


def top_ten(subreddit):

    """return the url"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'This agent?'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if response.status_code == 404:
        pirint("None")
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title']
        print(title)


if __name__ == '__main__':
    top_ten(subreddit)
