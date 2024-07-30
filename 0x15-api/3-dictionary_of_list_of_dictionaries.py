#!/usr/bin/python3
"""
use API for given employee and return info about task progress
"""

import json
import requests


url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    users = requests.get("{}/users".format(url)).json()
    todos = requests.get("{}/todos".format(url)).json()

    dictt = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')

        dictt[str(id)] = []
        for task in todos:
            if task.get("userId") == id:
                title = task.get('title')
                completed = task.get('completed')
                dictt[str(id)].append({
                                "username": username,
                                "task": title,
                                "completed": completed})

    with open('todo_all_employees.json', 'w') as jsf:
        json.dump(dictt, jsf)
