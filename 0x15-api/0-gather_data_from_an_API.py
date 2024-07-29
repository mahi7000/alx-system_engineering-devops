#!/usr/bin/python3
"""use REST API for a given employee id and return info about progress"""

import requests
import sys


if __name__ == "__main__":
    """import rest api for id"""
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) > 1:
        id = int(sys.argv[1])
        req1 = requests.get('{}users/{}'.format(url, id))
        req2 = requests.get('{}todos/'.format(url))

        if req1.status_code == 200 and req2.status_code == 200:
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

            print("Employee {} is done with tasks({}/{})".format(
                                        name, len(tasks), len(completed)))

            for task in completed:
                print("\t {}".format(task))
