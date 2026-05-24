import json
import os


FILE_NAME = "data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def Add_Newtask():
    t_name = input("Enter the task name: ")
    t_status = input("Enter task status (complete/incomplete): ")

    taskdata = {
        "task name": t_name,
        "task status": t_status
    }

    data = load_data()

    
    if not isinstance(data, list):
        data = []

   
    data.append(taskdata)

    save_data(data)

    print("Task added successfully!")



#VIEW TASK.....



def View_Task():
    data = load_data()

    if not data:
        print("No tasks found!")
        return

    for i, task in enumerate(data, start=1):
        if isinstance(task, dict):
            print(f"\nTask {i}")
            print("Name   :", task.get("task name"))
            print("Status :", task.get("task status"))
        else:
            print(f"\nInvalid task format: {task}")
 
#update task.....
def Update_Task():
    data = load_data()

    if not isinstance(data, list):
        print("Data corrupted! Resetting...")
        data = []

    name = input("Enter task name to update: ")
    new_status = input("Enter status (complete/incomplete): ")

    found = False

    for task in data:
        if isinstance(task, dict): 
            if task.get("task name", "").lower() == name.lower():
                task["task status"] = new_status
                found = True
                break

    if found:
        save_data(data)
        print("Task updated successfully!")
    else:
        print("Task not found!")


#delete...
def Delete():
    data = load_data()

    if not data:
        print("No tasks to delete!")
        return

    View_Task()

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if index < 0 or index >= len(data):
            print("Invalid task number!")
            return

        removed = data.pop(index)

        save_data(data)
        print(f"Task '{removed['task name']}' deleted successfully!")

    except ValueError:
        print("Invalid input!")
