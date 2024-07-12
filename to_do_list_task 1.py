def display_menu():
    print("Welcome to the To-Do List App!")
    print("Please select an option:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks(tasks):
    print("Current tasks:")
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i + 1}. {status} {task['description']}")


def add_task(tasks):
    task_description = input("Enter the task description: ")
    tasks.append({"description": task_description, "completed": False})
    print("Task added successfully!")


def mark_complete(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to delete: "))
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Deleted task: {deleted_task['description']}")
    else:
        print("Invalid task number.")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()