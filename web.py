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


for fromuser in todos:
    option = st.checkbox(fromuser)

st.text_input(label=" ", placeholder="enter todo...", key="new_todo", on_change=add_todo)
