user_prompt = "Enter a todo:"
todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print("Todo list: ", todos)