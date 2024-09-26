import functions

import FreeSimpleGUI as sg

label = sg.Text("Start by typing a todo...")

input_box = sg.InputText(tooltip="Type here")

add_button = sg.Button("Add")

window = sg.Window("The Really Cool Todo App", layout=[[label],[input_box,add_button]])




window.read()
window.close()