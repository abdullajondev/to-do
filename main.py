

while True:
    user_action = input("Type: add, show,complete, edit, exit:  ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("inter to do: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index}-{item}"
                print(row)
        case 'edit':
            number = int(input('please enter the number you wont to edit:  '))
            number = number - 1
            new_todo = input("pls enter new todo")
            todos[number] = new_todo
        case 'complete': 
            number = int(input("plase enter the task you complete: "))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Hey You entered unknown word")
