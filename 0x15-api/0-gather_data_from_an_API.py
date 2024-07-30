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

        name = users.get("name")
        tasks = []
        completed = []

        for task in todos:
            if task.get("userId") == id:
                tasks.append(task.get("title"))
                if task.get("completed"):
                    completed.append(task.get("title"))

        print("Employee {} is done with tasks({}/{}):".format(
                                        name, len(completed), len(tasks)))

        for task in completed:
            print("\t {}".format(task))
