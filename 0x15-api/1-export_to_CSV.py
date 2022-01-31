#!/usr/bin/python3
"""
requesting data from an api
export to csv
"""
import csv
from fileinput import filename
import requests
from sys import argv


def my_csv():
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

    filename = "{}.csv".format(argv[1])
    with open(filename, 'w') as csvfile:
        fieldnames = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for status in TASK_COMPLETED_STATUS:
            writer.writerow({"USER_ID": argv[1],
                             "USERNAME": EMPLOYEE_NAME,
                             "TASK_COMPLETED_STATUS": status[0],
                             "TASK_TITLE": status[1]})


if __name__ == '__main__':
    my_csv()
