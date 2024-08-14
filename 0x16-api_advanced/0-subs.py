#!/usr/bin/python3
"""Finds and returns the number of subscribers in a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """return the number of subs in {{subreddit}}"""
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"User-Agent": "Subs/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    subs = data.get("subscribers")
    return subs
