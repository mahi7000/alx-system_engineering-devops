#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """Titles of the first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'TopTen/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.get('data')
        children = data.get('children')
        
        for i in range(10):
            print(children[i].get('data').get('title'))
    else:
        print("None")
