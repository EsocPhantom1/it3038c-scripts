This script is a task manager that you can use as a planner on your laptop to help your day be more 
organized. I found this script useful because I had the notes app on my phone to plan out my school
work for the week but I did not have anything for my laptop so I decided to make a task manager that 
logged my task name, decription, and due date you can also use this script as a simple planner for 
upcoming events that you may hav going on in your life! This script uses a gui(tkinter) for a 
user friendly view.

As soon as the script is run a GUI will appear and  the first thing you should do is write the name 
of your task for example(FINAL). Next you want to write down the decription of your task in the 
decription box(IMPORTANT: Final project of the year). Finaly there is the Due Date where you can 
input the date your event expires(12/3/2023). Next you would click the "Add Task" button if you 
failed to input a task name or due date then you would get an error saying 
"Task name and due date are required.". If not then you would see your task fall to the list box.
If you want to see the decription of your task first click on your task and click the button 
"View Task Details". If you want to check your task as complete simpily click on the task and click 
the button "Mark as Completed", 
def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["Completed"] = True
            self.populate_task_listbox()
            self.save_tasks()
if you want to uncheck the task click on the task and click the 
"Uncheck Task" button.
def uncheck_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["Completed"] = False
            self.populate_task_listbox()
            self.save_tasks()
If you are compleatly done with the task then click the task and click the 
"Delete Task" button. 
def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.populate_task_listbox()
            self.save_tasks()
Even if you close out of the GUI or script and reopen it the Task Manager will 
remember what Tasks you had as long as you did not delete them via the "Delete Task" button of course.
def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
To be able to run this script make sure to use the pip command on your terminal to install your 
imports. pip install tkinter. Do the same for any other packages that you dont have. 
