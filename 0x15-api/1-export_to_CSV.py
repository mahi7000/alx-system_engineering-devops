#!/usr/bin/python3
"""
use API for given employee and return info about task progress
"""

import requests
import sys


url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        users = requests.get("{}/users/{}".format(url, id)).json()
        todos = requests.get("{}/todos".format(url)).json()

        name = users.get("username")
        tasks = []

        for task in todos:
            if task.get("userId") == id:
                tasks.append(task)

        with open('{}.csv'.format(id), 'w') as csvf:
            for task in tasks:
                completed = task.get("completed")
                title = task.get("title")

                csvf.write('"{}","{}","{}","{}"\n'.format(
                    id, name, completed, title))
