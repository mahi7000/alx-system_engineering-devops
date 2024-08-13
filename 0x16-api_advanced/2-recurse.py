#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """returns list of titles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "HotList/1.0"}

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = results.get('after')
    count += results.get('dist')
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
