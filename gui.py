import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('Black')

time_info = sg.Text('', key='time_info')
label = sg.Text("Start by typing a todo...")

input_box = sg.InputText(tooltip="Type here", key="todo")

add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 15])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

attribution = sg.Text("App icon by Shahid-Mehmood", font=0.5)

window = sg.Window("The Really Cool Todo App",
                   layout=[[time_info],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button],
                           [attribution]],
                   font=("Helvetica", 20))

exit_text = sg.Text("Thank you for using the Really Cool Todo App!")
ok_button = sg.Button("OK")
exit_window = sg.Window("Bye!", layout=[[exit_text], [ok_button]], font=("Helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or window.was_closed():
        break
    if not window.was_closed():
        window["time_info"].update(value=time.strftime("%A, %d %B %Y")+' - '+time.strftime("%H:%M"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()  # get the list
                index = todos.index(todo_to_edit)  # get the index you want to edit
                todos[index] = new_todo  # edit the todo
                functions.write_todos(todos)  # save the new updated list
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("You should select a todo to edit first...", title="Error", font=("Helvetica", 20))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                sg.popup("You should select a todo to edit first...", title="Error", font=("Helvetica", 20))
        case "Exit":
            event, values = exit_window.read()
            match event:
                case "OK":
                    exit_window.close()
            break
        case sg.WIN_CLOSED:
            event, values = exit_window.read()
            match event:
                case "OK":
                    exit_window.close()
            break

window.close()
