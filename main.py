

while True:
    user_action = input("Type: add, show,complete, edit, exit:  ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("inter to do: ") + "\n"

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

                todos.append(todo)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, item in enumerate(new_todos):
                item = item.title()
                index = int(index + 1)
                row = f"{index}-{item}"
                print(row)
        case 'edit':
            number = int(input('please enter the number you wont to edit:  '))
            number = number - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("pls enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        case 'complete': 
            number = int(input("plase enter the task you complete: "))
            index = number - 1
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.pop(index)
            todo_completed = todos[index].strip('\n')

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            message = f"todo {todo_completed} was removed from the list"
            print(message)
        case 'exit':
            break
        case _:
            print("Hey You entered unknown word")
