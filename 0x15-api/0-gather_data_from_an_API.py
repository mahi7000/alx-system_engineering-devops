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
        users = requests.get('{}/users/{}'.format(url, id)).json()
        todos = requests.get('{}/todos'.format(url)).json()

        name = users.get('name')
        tasks = list(filter(lambda x: x.get('userId') == id, todos))
        completed = list(filter(lambda x: x.get('completed'), tasks))

        print(
            "Employee {} is done with tasks({}/{}):".format(
                name,
                len(completed),
                len(tasks)
            )
        )

        for task in completed:
            print('\t {}'.format(task.get('title')))
