#!/usr/bin/python3
"""
requesting data from an api
export to json
"""
import json
import requests
from sys import argv


def to_json():
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = user.get('name')
            break

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    TASK_COMPLETED_STATUS = []
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TASK_COMPLETED_STATUS.append((todo.get('completed'),
                                          todo.get('title')))

    inside = []
    for status in TASK_COMPLETED_STATUS:
        inside.append({"task": status[1],
                       "completed": status[0],
                       "username": EMPLOYEE_NAME})
    data = {str(argv[1]): inside}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)

if __name__ == '__main__':
    to_json()
