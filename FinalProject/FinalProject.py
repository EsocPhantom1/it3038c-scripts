import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        
        self.tasks = []

        # Load tasks from file if available
        self.load_tasks()

        # Entry widgets
        self.task_name_entry = ttk.Entry(root, font=('Times New Roman', 12))
        self.task_description_entry = ttk.Entry(root, font=('Times New Roman', 12))
        self.due_date_entry = ttk.Entry(root, font=('Times New Roman', 12))

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=('Times New Roman', 12), selectmode=tk.SINGLE)
        self.populate_task_listbox()

        # Buttons
        ttk.Button(root, text="Add Task", command=self.add_task).grid(row=0, column=1, pady=10)
        ttk.Button(root, text="Mark as Completed", command=self.mark_as_completed).grid(row=1, column=1, pady=10)
        ttk.Button(root, text="Uncheck Task", command=self.uncheck_task).grid(row=1, column=0, pady=10)
        ttk.Button(root, text="Delete Task", command=self.delete_task).grid(row=0, column=0, pady=10)
        ttk.Button(root, text="View Task Details", command=self.view_task_details).grid(row=5, column=0, columnspan=2, pady=10)

        # Labels
        ttk.Label(root, text="Task Name:").grid(row=2, column=0, sticky='e')
        ttk.Label(root, text="Description:").grid(row=3, column=0, sticky='e')
        ttk.Label(root, text="Due Date:").grid(row=4, column=0, sticky='e')

        # Entry widgets placement
        self.task_name_entry.grid(row=2, column=1, pady=5)
        self.task_description_entry.grid(row=3, column=1, pady=5)
        self.due_date_entry.grid(row=4, column=1, pady=5)

        # Listbox placement
        self.task_listbox.grid(row=5, column=0, columnspan=2, pady=10, sticky='nsew')

        # Configure row and column weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(2):
            root.grid_columnconfigure(i, weight=1)

    def add_task(self):
        # Get values from entry widgets
        task_name = self.task_name_entry.get()
        task_description = self.task_description_entry.get()
        due_date = self.due_date_entry.get()

        if task_name and due_date:
            task = {"Name": task_name, "Description": task_description, "Due Date": due_date, "Completed": False}
            self.tasks.append(task)

            # Update listbox and clear entry widgets
            self.populate_task_listbox()
            self.clear_entry_widgets()

            # Save tasks to file
            self.save_tasks()
        else:
            messagebox.showerror("Error", "Task name and due date are required.")

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["Completed"] = True
            self.populate_task_listbox()
            self.save_tasks()

    def uncheck_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["Completed"] = False
            self.populate_task_listbox()
            self.save_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.populate_task_listbox()
            self.save_tasks()

    def view_task_details(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            details = f"Name: {task['Name']}\nDescription: {task['Description']}\nDue Date: {task['Due Date']}\nCompleted: {task['Completed']}"
            messagebox.showinfo("Task Details", details)

    def populate_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔" if task["Completed"] else " "
            self.task_listbox.insert(tk.END, f"{status} {task['Name']} ({task['Due Date']})")

    def clear_entry_widgets(self):
        self.task_name_entry.delete(0, tk.END)
        self.task_description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
