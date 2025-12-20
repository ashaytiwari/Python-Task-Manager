tasks = []

while True:
    user_action = input("Type add, show or exit: ")

    match user_action.strip():
        
        case "add":
            todo = input("Enter Task: ")
            tasks.append(todo)

        case "show":
            for item in tasks:
                print(item)

        case "exit":
            break
        
        case _:
            print('Hey you have entered an unknown command')
        
print('Bye, see you soon!')