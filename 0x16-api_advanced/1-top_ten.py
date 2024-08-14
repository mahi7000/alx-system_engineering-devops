#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """Titles of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'TopTen/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        data = response.get('data')
        children = data.get('children')

        for child in children:
            print(child.get('data').get('title'))
    except Exception:
        print("None")
