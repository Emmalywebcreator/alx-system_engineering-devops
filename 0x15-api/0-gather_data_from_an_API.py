#!/usr/bin/python3
"""Fetch TODO list progress for a given employee ID."""
import sys
import requests


def get_employee_todo_progress():
    """
    Fetches and displays the TODO list progress for a given employee
    ID from the command line.

    Outputs:
        Displays the number of completed tasks and total tasks,
        and the titles of completed tasks.
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(sys.argv[1])

    user_response = requests.get('{0}/users/{1}'.format(url, employee_id))
    user = user_response.json()

    params = {'userId': employee_id}
    todos_response = requests.get('{0}/todos'.format(url), params=params)
    todos_data = todos_response.json()

    completed_tasks = [
        todo.get('title') for todo in todos_data if todo.get('completed')
    ]

    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print("Employee {0} is done with tasks({1}/{2}):".format(
        user.get('name'), number_of_done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {0}".format(task))


if __name__ == "__main__":
    get_employee_todo_progress()
