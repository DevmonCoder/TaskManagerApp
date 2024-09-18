from gui import TaskManagerApp
from Task import Task
from TasksManager import TaskManager
from Task import Task
import tkinter as tk

if __name__ == "__main__":
    manage = TaskManager()
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

    while True:
        print("\nWhat would you like to do?")
        print("\n1. List tasks")
        print("\n2. Create a new task")
        print("\n3. Edit a task")
        print("\n4. Delete a task")
        print("\n5. Exit")

        option = input("\nChoose an option:\n\t")

        if option == '1':
            manage.list_tasks()
        elif option == '2':
            title = input("\nTask:\n\t")
            description = input("\nDescription:\n\t")
            expiration_date = input("\nExpiration Date:\n\t")
            priority = input("\nPriority:\n\t")
            manage.create_task(title, description, expiration_date, priority)
        elif option == '3':
            try:
                index = int(input("\nTask Number to Edit:\n\t"))
                title = input("\nNew Title:\n\t")
                description = input("\nNew Description:\n\t")
                expiration_date = input("\nNew Expiration Date:\n\t")
                priority = input("\nPriority:\n\t")
                manage.edit_task(index, title=title, description=description, expiration_date=expiration_date, priority=priority)
            except ValueError:
                print("\nError:\nYou must enter an integer greater than zero")
        elif option == '4':
            try:
                index = int(input("\nTask Number to Delete:\n\t"))            
                manage.delete_task(index)
            except ValueError:
                print("\nError:\nYou must enter an integer greater than zero")
        elif option == '5':
            break
        else:
            print("Opción no válida!")