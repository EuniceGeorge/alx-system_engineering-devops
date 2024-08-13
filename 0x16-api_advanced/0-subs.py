#!/usr/bin/python3
""" Query RedditAPi to get total subscribers"""

import requests

def number_of_subscribers(subreddit):

    """return the url"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'This agent?'}

    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 404:
        return 0
    return data['data']['subscribers']


if __name__ == '__main__':
    number_of_subscribers(subreddit)
