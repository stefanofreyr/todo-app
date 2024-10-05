def get_todos(filepath="todos.txt"):
    """ Makes a list out of the contents of a .txt file, and returns that list."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """ Re-writes a list on a .txt file"""
    with open(filepath, 'w') as file:  # file is now in write mode
        file.writelines(todos_arg)  # writes updated list on file, one item per line

if __name__ == "__main__":
    print("Hello from 'functions'!")