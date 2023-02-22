import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My todo app")
st.subheader("this is my todo app")
st.write("this app icrease your productivity")


for index, todo in enumerate(todos):
    option = st.checkbox(todo, key=todo)
    if option:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="enter todo...", key="new_todo", on_change=add_todo)
