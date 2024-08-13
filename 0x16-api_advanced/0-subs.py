#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the nubmer of subscribers or 0"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'UserAgent/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    except Exception:
        return 0
