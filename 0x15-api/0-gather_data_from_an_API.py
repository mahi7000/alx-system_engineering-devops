#!/usr/bin/python3
'''
use REST API for a given employee id and return info about progress
'''

import requests
import sys

url = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        req1 = requests.get('{}/users/{}'.format(url, id))
        req2 = requests.get('{}/todos'.format(url))

        users = req1.json()
        todos = req2.json()

        name = users['name']
        tasks = []
        completed = []

        for task in todos:
            if task.get("userId") == id:
                tasks.append(task["title"])
                if task["completed"]:
                    completed.append(task["title"])

        print("Employee {} is done with tasks({}/{}):".format(
                                    name, len(completed), len(tasks)))

        for task in completed:
            print("\t {}".format(task))
