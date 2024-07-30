#!/usr/bin/python3
"""
use API for given employee and return info about task progress
"""

import json
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

        dictt = {str(id): []}
        for task in todos:
            if task.get("userId") == id:
                tasks.append(task)
                title = task.get('title')
                completed = task.get('completed')
                dictt[str(id)].append({
                                "task": title,
                                "completed": completed,
                                "username": name})

        with open('{}.json'.format(id), 'w') as jsf:
            json.dump(dictt, jsf)
