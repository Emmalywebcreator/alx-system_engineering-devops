import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.
    
    Args:
        employee_id (int): The ID of the employee to fetch the TODO list for.
    
    Outputs:
        Displays the employee's name, number of completed tasks, total tasks,
        and the titles of completed tasks.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee details
    employee_response = requests.get(f'{base_url}/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch employee's todo list
    todos_response = requests.get(f'{base_url}/todos', params={'userId': employee_id})
    todos_data = todos_response.json()

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_data)
    done_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(done_tasks)

    # Print the employee TODO list progress
    print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):')
    for task in done_tasks:
        print(f'\t {task}')

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

