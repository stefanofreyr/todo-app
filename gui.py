from typing import List

import functions

import FreeSimpleGUI as sg

label = sg.Text("Start by typing a todo...")

input_box = sg.InputText(tooltip="Type here", key="todo")

add_button = sg.Button("Add")

window = sg.Window("The Really Cool Todo App",
                   layout=[[label],[input_box,add_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED():
            break

window.close()