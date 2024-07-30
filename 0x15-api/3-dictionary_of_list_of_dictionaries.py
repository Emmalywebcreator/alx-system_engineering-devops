#!/usr/bin/python3
"""Fetch TODO list progress for all employees and export to JSON."""
import json
import requests


def get_all_employees_todo_progress():
    """
    Fetches and displays the TODO list progress for all employees
    and exports the data to a JSON file.

    Outputs:
        Exports the data in JSON format containing all tasks for all employees.
    """
    url = 'https://jsonplaceholder.typicode.com'

    users_response = requests.get('{}/users'.format(url))
    users_data = users_response.json()

    todos_response = requests.get('{}/todos'.format(url))
    todos_data = todos_response.json()

    all_tasks = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        user_tasks = [{
            "username": username,
            "task": todo.get('title'),
            "completed": todo.get('completed')
        } for todo in todos_data if todo.get('userId') == user_id]

        all_tasks[str(user_id)] = user_tasks

    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    get_all_employees_todo_progress()
