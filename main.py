##from modules.functions import get_todos, write_todos
from modules import functions


while True:
    user_action = input("Type: add, show,complete, edit, exit:  ")
    user_action = user_action.strip()

    if 'add' in user_action:
        try:
            todo = user_action[3:] + "\n"

            todos = functions.get_todos()

            todos.append(todo)

            functions.write_todos(todos)
        except ValueError:
            print("your commend is not valid")
            continue
    elif 'show' in user_action:
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        try:
            number = int(user_action[4:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("pls enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("your commend is not valid")
    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_completed = todos[index].strip('\n')
            todos.pop(index)


            functions.write_todos(todos)
            message = f"todo {todo_completed} was removed from the list"
            print(message)
        except IndexError:
            print("your commend is not valid")
        continue
    elif 'exit' in user_action:
        break
    else:
        print("Hey You entered unknown word")
