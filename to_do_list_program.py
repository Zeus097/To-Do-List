



# It's not included in My GitHub


def main_menu():
    print("\n ----- To-Do List📝 -----")
    print("1. Add a new task 📌")
    print("2. Mark a task as completed 🟢")
    print("3. View all tasks 📝")
    print("4. Quit the program 🔴")

def add_task(todo_list):
    task = input("Type your task here: ")
    todo_list.append(task)
    print("Task added successfully!")
def mark_as_completed(todo_list):
    print("-----< TASKS📝 >-----")
    index = int(input("Type the Index of the task for completion (0-...): "))
    for i, task in enumerate(todo_list):
        if i == index:
            print("Task completed successfully 🟢, removed from the list !")
            todo_list.remove(task)
        else:
            print("Invalid Index. Your task is not marked yet!")


def view_all(todo_list):
    print("-----< REMAINING TASKS📝 >-----")
    if len(todo_list) > 0:
        print("  <>  ".join(todo_list))
    else:
        print("Empty.")
def todo_list_program():
    todo_list = []


    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(todo_list)
        if choice == "2":
            mark_as_completed(todo_list)
        if choice == "3":
            view_all(todo_list)
        if choice == "4":
            print("Exiting the program, Bye Bye!")
            break

todo_list_program()
