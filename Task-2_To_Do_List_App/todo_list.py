tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def list_tasks():
    for i, t in enumerate(tasks):
        status = "✓" if t["completed"] else "✗"
        print(f"{i + 1}. [{status}] {t['task']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. List Tasks\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(input("Enter task: "))
        elif choice == '2':
            complete_task(int(input("Enter task number to complete: ")) - 1)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")