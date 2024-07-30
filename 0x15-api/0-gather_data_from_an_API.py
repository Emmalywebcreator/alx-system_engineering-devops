import sys
import requests


def get_employee_todo_progress():
    """
    Fetches and displays the TODO list progress for a given employee ID from the command line.

    Outputs:
        Displays the number of completed tasks and total tasks,
        and the titles of completed tasks.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    employee_id = int(sys.argv[1])
    employee_response = requests.get('{}/users/{}'.format(base_url, employee_id))
    employee_data = employee_response.json()
    params = {'userId': employee_id}

    todos_response = requests.get('{}/todos'.format(base_url), params=params)
    todos_data = todos_response.json()

    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print('Employee is done with tasks({}/{}):'.format(
        number_of_done_tasks, total_tasks
    ))
    for task in completed_tasks:
        print('\t {}'.format(task))


if __name__ == "__main__":
    get_employee_todo_progress()
