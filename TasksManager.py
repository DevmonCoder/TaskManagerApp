from Task import Task
from collections import deque
import json

# This class allows creating, reading and listing tasks
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_path = 'tasks.json' # File where the tasks will be saved
        self.load_tasks() # Load tasks at startup

    def create_task(self, title, description, expiration_date, priority):
        task = Task(title, description, expiration_date, priority)
        self.add_task(task)
        print(f"Task {task} successfully created.")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks() # Save the tasks after adding them

    def save_tasks(self):
        try:
            # Save the tasks in a JSON file
            with open(self.file_path, 'w') as file: # Overwrite the file every time the tasks are saved and automatically close the file once the tasks are finished writing
                json_tasks = [task.__dict__ for task in self.tasks] # Convert the task list (in dictionary format) to JSON and write them to the file
                json.dump(json_tasks, file, indent=4) # Write the serialized data (converted to JSON) in the specified file
            print(f"Task saved successfully in {self.file_path}")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file: # Read the file to load the saved tasks and automatically close the file once the tasks are finishing loading
                self.tasks = [] # Clear the task list before loading
                json_tasks = json.load(file) # Read the file and convert the JSON content back to a list of dictionaries
                for task_data in json_tasks:
                    task = Task(**task_data) # Create Task objects from the dictionary
                    self.tasks.append(task)
            print("Task loaded successfully")
        except FileNotFoundError:
            print("No saved tasks were found")
        except Exception as e:
            print(f"Error loading tasks")

    def list_tasks(self):
        if not self.tasks:
            print("There aren't pending tasks")
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
            print("Task successfully edited")
        except IndexError:
            print("The task doesn't exist")
    
    def delete_task(self, index):
        try:
            self.tasks.pop(index - 1)
            self.save_tasks()
            print("Task successfully deleted.")
        except IndexError:
            print("The task doesn't exist")

# 1. Create an instance of TaskManager (this will load the saved tasks)
manage = TaskManager()

# 2. List loaded tasks when starting the application
print("Tasks loaded at startup:")
manage.list_tasks()

# 3. Create new tasks
manage.create_task("Code an application in Java", "Find a problem to solve using Java", "2024-09-13", "High")
manage.create_task("Code an application in C++", "Find a problem to solve using C++", "2024-09-14", "High")
manage.create_task("Study agile methodology", "Apply the SCRUM framework and the Kanban System", "2024-09-15", "High")
manage.create_task("Increase visibility on social media", "GitHub, Discord, LinkedIn", "2024-09-16", "High")
manage.create_task("Gain visibility on LinkedIn", "Publish tech articles on LinkedIn", "2024-09-17", "High")

# 4. Save the tasks in the JSON file
manage.save_tasks()

manage.list_tasks()

# 5. List the tasks after adding new ones
print("Tasks after adding:")
manage.list_tasks()

# 6. Edit a task (for example, change the description of the first task)
manage.edit_task(1, description="Design graphical interface")
manage.save_tasks()  # Save the changes

# 7. List the tasks after the edit
print("Tasks after editing the first task:")
manage.list_tasks()

# 8. Delete the first task
manage.delete_task(1)
manage.save_tasks()  # Save the changes

# 9. List the tasks after deleting a task
print("Tasks after deleting the first task:")
manage.list_tasks()

# 10. Close and restart the application (simulated)
# Restarting the application would be running the script again.
# This will reload the tasks from the JSON file.
manage = TaskManager()
print("Tasks after restarting the application:")
manage.list_tasks()