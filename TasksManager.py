from Task import Task
from collections import deque
import json

# This class allows creating, reading and listing tasks
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_path = 'tasks.json' # File where the tasks will be saved
        self.load_tasks() # Load tasks at startup
        self.tasks = []

    def get_all_tasks(self):
        return self.tasks        

    def create_task(self, title, description, expiration_date, priority):
        task = Task(title, description, expiration_date, priority)
        self.add_task(task)
        print(f"\nTask {task} successfully created.")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks() # Save the tasks after adding them

    def save_tasks(self):
        try:
            # Save the tasks in a JSON file
            with open(self.file_path, 'w') as file: # Overwrite the file every time the tasks are saved and automatically close the file once the tasks are finished writing
                json_tasks = [task.__dict__ for task in self.tasks] # Convert the task list (in dictionary format) to JSON and write them to the file
                json.dump(json_tasks, file, indent=4) # Write the serialized data (converted to JSON) in the specified file
            print(f"\nTask saved successfully in {self.file_path}")
        except Exception as e:
            print(f"\nError saving tasks: {e}")

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file: # Read the file to load the saved tasks and automatically close the file once the tasks are finishing loading
                self.tasks = [] # Clear the task list before loading
                json_tasks = json.load(file) # Read the file and convert the JSON content back to a list of dictionaries
                for task_data in json_tasks:
                    task = Task(**task_data) # Create Task objects from the dictionary
                    self.tasks.append(task)
            print("\nTask loaded successfully")
        except FileNotFoundError:
            print("\nNo saved tasks were found")
        except Exception as e:
            print(f"\nError loading tasks")

    def list_tasks(self):
        if not self.tasks:
            print("\nThere aren't pending tasks")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def edit_task(self, index, title=None, description=None, expiration_date=None, priority=None):
        try:
            task = self.tasks[index - 1]
            task.title = title if title else task.title
            task.description = description if description else task.description
            task.expiration_date = expiration_date if expiration_date else task.expiration_date
            task.priority = priority if priority else task.priority
            self.save_tasks()
            print("\nTask successfully edited")
        except IndexError:
            print("\nThe task doesn't exist")
    
    def delete_task(self, index):
        try:
            self.tasks.pop(index - 1)
            self.save_tasks()
            print("\nTask successfully deleted.")
        except IndexError:
            print("\nThe task doesn't exist")