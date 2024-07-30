mport requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error fetching user with ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching TODO list for user with ID {employee_id}")
        return

    todos_data = todos_response.json()
    
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    """
    Main entry point of the script. Expects an employee ID as a command-line argument.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

