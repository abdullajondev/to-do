import functions
import PySimpleGUI as sg

"""if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", "w") as file:
        pass"""

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", mouseover_colors="LightBlue2")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("exit")
sg.theme('Black')


window = sg.Window('MY to-do app', layout=[[label],
                                           [input_box, add_button],
                                           [list_box, edit_button, complete_button],
                                           [exit_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                # print(todo_to_edit)
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please enter an item first.", font=("Helvetica", 20))
        case "complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value=" ")
            except IndexError:
                sg.popup("please enter an item first.", font=("Helvetica", 20))
        case "exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])


        case sg.WINDOW_CLOSED:
            break



window.close()