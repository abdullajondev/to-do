
def get_todos(filepath):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

while True:
    user_action = input("Type: add, show,complete, edit, exit:  ")
    user_action = user_action.strip()

    if 'add' in user_action:
        try:
            todo = user_action[3:] + "\n"

            todos = get_todos("files/todos.txt")

            todos.append(todo)

            write_todos("files/todos.txt", todos)
        except ValueError:
            print("your commend is not valid")
            continue
    elif 'show' in user_action:
        todos = get_todos("files/todos.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        try:
            number = int(user_action[4:])
            number = number - 1

            todos = get_todos("files/todos.txt")

            new_todo = input("pls enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("files/todos.txt", todos)
        except ValueError:
            print("your commend is not valid")
    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = get_todos("files/todos.txt")

            todo_completed = todos[index].strip('\n')
            todos.pop(index)


            write_todos("files/todos.txt", todos)
            message = f"todo {todo_completed} was removed from the list"
            print(message)
        except IndexError:
            print("your commend is not valid")
        continue
    elif 'exit' in user_action:
        break
    else:
        print("Hey You entered unknown word")
