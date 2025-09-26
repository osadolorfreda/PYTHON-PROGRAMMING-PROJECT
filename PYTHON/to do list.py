def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()