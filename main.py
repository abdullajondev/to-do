

while True:
    user_action = input("Type: add, show,complete, edit, exit:  ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[3:] + "\n"

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)
        print(todos)
        print(todo)
    elif 'show' in user_action:
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[4:])
        number = number - 1

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("pls enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("files/todos.txt", "w") as file: 
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[8:])
        index = number - 1
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.pop(index)
        todo_completed = todos[index].strip('\n')

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
        message = f"todo {todo_completed} was removed from the list"
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Hey You entered unknown word")
