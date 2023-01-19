import sys

file_name = "todo_data.txt"
todos = []

# Read file
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

print(todos)

# Add Todo
if len(sys.argv) >= 3 and sys.argv[1] == "add":
    todos.append(f"\n{sys.argv[2]}")

# Remove Todo
if len(sys.argv) >= 3 and sys.argv[1] == "remove":
    try:
        index_to_delete = sys.argv[2]
        print(index_to_delete)
        for todo in todos:
            print(todo)
            if todo == f"{index_to_delete}\n":
                del (todo)
            else:
                continue
        # if index_to_delete > 0:
        #     index_to_delete -= 1
        #     del (todos[index_to_delete])
    except Exception as e:
        print(e)
        sys.exit(1)


print(todos)

# Save File
file = open(file_name, "w")
file.writelines(todos)
file.close()

# Print List
# print("\nHere's your ToDo List:\n")
# print("1. Walk the dog")
# print("2. Buy cheese")

# Print Commands
# print("\n***************************\n")
# print(f"To view ToDos:\n{sys.argv[0]}")
# print(f"\nTo add a ToDo:\n{sys.argv[0]} add \"Clean Room\"\n")
# print(f"To remove or complete ToDo:\n{sys.argv[0]} remove 2\n")
