import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from TasksManager import TaskManager
from Task import Task

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TASK MANAGER")
        self.root.geometry("600x400")
        # Frame to text inputs
        entry_frame = tk.Frame(root)
        entry_frame.pack(pady=10)
        # Labels and inputs fields
        tk.Label(entry_frame, text="Title:").grid(row=0, column=0)
        self.task_title_entry = tk.Entry(entry_frame)
        self.task_title_entry.grid(row=0, column=0)
        tk.Label(entry_frame, text="Description:").grid(row=1, column=0)
        self.task_description_entry = tk.Entry(entry_frame)
        self.task_description_entry.grid(row=1, column=0)
        tk.Label(entry_frame, text="Expiration Date:").grid(row=2, column=0)
        self.task_expiration_date_entry = tk.Entry(entry_frame)
        self.task_expiration_date_entry.grid(row=2, column=0)
        tk.Label(entry_frame, text="Priority:").grid(row=3, column=0)
        self.task_priority_entry = tk.Entry(entry_frame)
        self.task_priority_entry.grid(row=3, column=0)
        # Create a task list with a 'Listbox'
        self.tasks_listbox = tk.Listbox(self.root, height=15, width=50)
        self.tasks_listbox.pack(pady=20)
        # Call load_tasks
        self.load_tasks()
        #Buttons to add and delete tasks
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        self.add_task_btn = tk.Button(btn_frame, text="Agregar Tarea", command=self.add_task)
        self.add_task_btn.grid(row=0, column=0, padx=10)
        self.delete_task_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_btn.grid(row=0, column=1, padx=10)
    def load_tasks(self):
        task_manager = TaskManager()
        tasks = task_manager.get_all_tasks()
        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task['title']} - {task['due_date']}")
    def add_task(self):
        title = self.task_title_entry.get()
        description = self.task_description_entry.get()
        if not title or not description:
            print("Por favor, ingrese un titulo y una descripción.")
            return
        new_task = Task(title, description)
        self.task_manager.add_task(new_task)
        print(f"Task {title} added successfully!")
    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task_to_delet = self.task_list.get(selected_task_index)
            self.task_manager.delete_task(task_to_delet)
            self.task_list.delete(selected_task_index)
        else:
            messagebox.showwarning("Selección requerida", "Por favor")