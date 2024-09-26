from functions import get_todos, write_todos
import time

print("Welcome to the Really Cool Todo App!")
print("It is "+time.strftime("%A, %d %B %Y"))
print("Local time is "+time.strftime("%H:%M"))

while True:
    user_action = input("""Type 'add' followed by the task you want to add, 'show',
    'edit' followed by the number of the task you want to edit,
    'complete' followed by the number of the task you want to mark as done, or 'exit': """)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = get_todos()    # this makes a list out of the file's contents

        todos.append(todo)          # now that we have it as a list, we can add items

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            print(index+1, item.strip('\n'))

    elif user_action.startswith("edit"):
        todos = get_todos()
        try:
            number = int(user_action[5:])

            while number == 0 or number not in range(len(todos)+1):
                number = int(input("This is not a valid number. Please enter a valid number: "))
            todos[number-1] = input("Edit the todo: ") + '\n'

            write_todos(todos)

            print("Item edited successfully!")
        except ValueError:
            print("Your command is not valid...")
            continue

    elif user_action.startswith("complete"):
        todos = get_todos()

        try:
            number = int(user_action[9:])
            while number == 0 or number not in range(len(todos)+1):
                number = int(input("This is not a valid number. Please enter a valid number: "))
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"'{todo_to_remove}' has been marked as completed! Great job!")

        except ValueError:
            print("Your command is not valid...")
    elif user_action.startswith("exit"):
        break

    else:
        print("This is not a valid command.")

print("Thanks for using the Really Cool Todo App!")
