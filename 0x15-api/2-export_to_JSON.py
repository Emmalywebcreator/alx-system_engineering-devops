#!/usr/bin/python3
"""Fetch TODO list progress for a given employee ID and export to JSON."""
import json
import requests
import sys


def get_employee_todo_progress():
    """
    Fetches and displays the TODO list progress for a given employee
    ID from the command line and exports the data to a JSON file.

    Outputs:
        Displays the number of completed tasks and total tasks,
        and the titles of completed tasks.
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(sys.argv[1])

    user_response = requests.get('{}/users/{}'.format(url, employee_id))
    user = user_response.json()

    params = {'userId': employee_id}
    todos_response = requests.get('{}/todos'.format(url), params=params)
    todos_data = todos_response.json()

    completed_tasks = [
        todo.get('title') for todo in todos_data if todo.get('completed')
    ]

    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))

    # Export to JSON
    tasks = [{
        "task": todo.get('title'),
        "completed": todo.get('completed'),
        "username": user.get('username')
    } for todo in todos_data]

    json_data = {str(employee_id): tasks}
    json_filename = '{}.json'.format(employee_id)

    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    get_employee_todo_progress()
