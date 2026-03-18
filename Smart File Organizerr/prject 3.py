import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"❌ Deleted: {removed}")
    except:
        print("Invalid input!")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO APP ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Bye 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()