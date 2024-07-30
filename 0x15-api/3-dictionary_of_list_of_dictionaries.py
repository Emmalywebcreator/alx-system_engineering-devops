import requests
import json


def get_all_employees_todo():
    """
    Fetch and export the TODO list data for all employees.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_url = "{}/users".format(base_url)
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Error fetching users")
        return

    users_data = users_response.json()

    # Dictionary to hold all tasks for all employees
    all_tasks = {}

    # Fetch TODO list for each employee
    for user in users_data:
        employee_id = user.get('id')
        employee_name = user.get('username')

        todos_url = "{}/todos?userId={}".format(base_url, employee_id)
        todos_response = requests.get(todos_url)
        if todos_response.status_code != 200:
            print("Error fetching TODO list for user with ID {}".format(employee_id))
            continue

        todos_data = todos_response.json()

        tasks = [
            {
                "username": employee_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos_data
        ]
        all_tasks[str(employee_id)] = tasks

    # Export to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    get_all_employees_todo()

