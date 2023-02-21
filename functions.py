FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of to do items"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main":
    print("hello from functions")

