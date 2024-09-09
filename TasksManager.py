from Task import Task
from collections import deque

# This class allows creating, reading and listing tasks
class TaskManager:
    def __init__(self):
        self.task_list = []

    def create_task(self, title, description, expiration_date, priority):
        new_task = Task(title, description, expiration_date, priority)
        self.task_list.append(new_task)
        print("Task successfully created.")

    def list_tasks(self):
        if not self.task_list:
            print("There aren't pending tasks")
        else:
            for i, task in enumerate(self.task_list, 1):
                print(f"{i}. {task}")

    def edit_task(self, index, title=None, description=None, expiration_date=None, priority=None):
        try:
            task = self.task_list[index - 1]
            task.title = title if title else task.title
            task.description = description if description else task.description
            task.expiration_date = expiration_date if expiration_date else task.expiration_date
            task.priority = priority if priority else task.priority
            print("Task successfully edited")
        except IndexError:
            print("The task doesn't exist")
    
    def delete_task(self, index):
        try:
            self.task_list.pop(index - 1)
            print("Task successfully deleted.")
        except IndexError:
            print("The task doesn't exist")

manage = TaskManager()
manage.create_task("Buy food", "Go to the supermarket", "2024-09-10", "High")
manage.create_task("Buy more food", "Go again to the supermarket", "2024-09-12", "Low")
manage.list_tasks()
manage.edit_task(1, description="SUPERMARKET FRUIT")
manage.list_tasks()
manage.delete_task(1)
manage.list_tasks()