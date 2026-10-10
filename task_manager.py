todo = {}

def add():
    while True:
        task = input("Enter Task Name (DONE to Exit): ")
        if task.upper() == 'DONE':
            break
        if task in todo:
            print(f"Task '{task}' already exists!")
            continue
        detail = input("Enter Task Details: ")
        todo[task] = detail
        print(f"Task '{task}' Added Successfully!")

def view():
    if len(todo) == 0:
        print("\nYour Todo List is Empty!")
        return
    print("\n========= YOUR TODO LIST =========")
    for i, (task, detail) in enumerate(todo.items(), 1):
        print(f"{i}. {task} → {detail}")
    print("==================================")

def update():
    view()
    if len(todo) == 0:
        return
    task = input("Enter Task Name to Update: ")
    if task in todo:
        detail = input("Enter New Details: ")
        todo[task] = detail
        print(f"Task '{task}' Updated Successfully!")
    else:
        print(f"Task '{task}' Not Found!")

def delete():
    view()
    if len(todo) == 0:
        return
    task = input("Enter Task Name to Delete: ")
    if task in todo:
        todo.pop(task)
        print(f"Task '{task}' Deleted Successfully!")
    else:
        print(f"Task '{task}' Not Found!")

def menu():
    print("\n========= TODO APP =========")
    print("1 → Add Task")
    print("2 → View Tasks")
    print("3 → Update Task")
    print("4 → Delete Task")
    print("9 → Exit")
    print("============================")

# Main Loop
option = 0
while option != 9:
    menu()
    try:
        option = int(input("Enter Your Choice: "))

        if option == 1:
            add()
        elif option == 2:
            view()
        elif option == 3:
            update()
        elif option == 4:
            delete()
        elif option == 9:
            print("Goodbye! App Closing...")
        else:
            print("Invalid Option! Please Choose 1, 2, 3, 4 or 9")

    except ValueError:
        print("Invalid Input! Please Enter a Number!")