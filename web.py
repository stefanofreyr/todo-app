import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("The ***Really Cool*** Todo App")
st.subheader("Made by Stefano Freyr Castiglione")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

add_button = st.button(label="Add",icon=":material/add:",use_container_width=True)

if add_button:
    st.text_input(label="",placeholder="Add a todo",
                  on_change=add_todo,key="new_todo")


