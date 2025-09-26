import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added!')

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Task "{removed_task}" deleted!')
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nPersonal Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                task_index = int(input("Enter the task number to delete: ")) - 1
                delete_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the task manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()