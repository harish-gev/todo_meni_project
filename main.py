from untitled import Add_Newtask 
from untitled import View_Task
from untitled import Update_Task
from untitled import Delete
def menu():
    while True:
        print("\n--- task manager---")
        print("1. Add new task")
        print("2. view task")
        print("3. update task status")
        print("4. delete the task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1" or choice == "add new task":
            Add_Newtask()

        elif choice == "2" or choice=="view task" :
            View_Task()

        elif choice == "3" or choice=="update task status" :
            Update_Task()
        
        elif choice == "4" or choice=="delete" :
            Delete()
        
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

menu()
