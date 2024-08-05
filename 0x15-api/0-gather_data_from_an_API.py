#!/usr/bin/python3
"""A python script that prints iformation using API
"""
import requests
import sys

if __name__ == "__main__":

    argv = sys.argv
    if len(argv) < 2:
        exit()

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(url)
    json_response = response.json()
    name = json_response.get("name")
    emp_id = json_response.get("id")

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    todo_response = requests.get(todo_url)
    todo_response_json = todo_response.json()
    todo_task = []

    for task in todo_response_json:
        if task.get("userId") == emp_id:
            todo_task.append(task)

    completed_task = 0

    for task in todo_task:
        if task.get("completed") is True:
            completed_task += 1

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed_task, len(todo_task)))

    for title in todo_task:
        if title.get("completed") is True:
            print("\t {}".format(title.get("title")))
