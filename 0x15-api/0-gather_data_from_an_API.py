import sys
import requests


def get_employee_todo_progress():
    """
    Fetches and displays the TODO list progress for a given employee ID from the command line.

    Outputs:
        Displays the number of completed tasks and total tasks,
        and the titles of completed tasks.
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(sys.argv[1])
    
    user_response = requests.get(url + '/users/{}'.format(employee_id))
    user = user_response.json()
    
    params = {'userId': employee_id}
    todos_response = requests.get(url + '/todos', params=params)
    todos_data = todos_response.json()
    
    completed_tasks = []
    for todo in todos_data:
        if todo.get('completed') is True:
            completed_tasks.append(todo.get('title'))

    total_tasks = len(todos_data)
    number_of_done_tasks = len(completed_tasks)

    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
        number_of_done_tasks, total_tasks
    ))
    for task in completed_tasks:
        print('\t {}'.format(task))


if __name__ == "__main__":
    get_employee_todo_progress()

