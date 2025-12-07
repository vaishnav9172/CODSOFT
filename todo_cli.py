tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task Completed")
    print("5. Delete Task")
    print("6. Exit")
    print("=============================")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("✔ Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available!")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks):
        status = "✔ Done" if t["done"] else "✘ Pending"
        print(f"{i + 1}. {t['task']} - {status}")

def update_task():
    view_tasks()
    num = int(input("Enter task number to update: ")) - 1
    new_task = input("Enter updated task: ")
    tasks[num]["task"] = new_task
    print("✔ Task updated!")

def complete_task():
    view_tasks()
    num = int(input("Enter task number to mark completed: ")) - 1
    tasks[num]["done"] = True
    print("✔ Task marked as completed!")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: ")) - 1
    tasks.pop(num)
    print("✔ Task deleted!")

# MAIN LOOP
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        complete_task()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again!")
