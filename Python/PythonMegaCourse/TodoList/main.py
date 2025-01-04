todos = []

while True:
    user_action = input("Enter 'Add', 'Show', or 'Exit': ")
    
    match user_action:
        case "Add":
            todo = input("Enter a todo:")
            todos.append(todo)
        case "Show":
            print("Todo list: ", todos)
        case "Exit":
            break

print("Goodbye")