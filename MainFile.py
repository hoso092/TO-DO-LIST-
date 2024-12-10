import tkinter as tk
import re
from tkinter import messagebox


class Task:
    def __init__(self, TaskDescription, Due_Date ,Priority) :
        self.TaskDescription = TaskDescription
        self.Due_Date = Due_Date
        self.Priority = Priority

class ToDoApp(Task):

    def __init__(self, root,TaskDescription="", Due_Date="", Priority=""):
        self.taskslist = []
        super().__init__(TaskDescription, Due_Date, Priority)
        self.root = root
        self.root.title("To-Do List App")

        # Task list display
        self.task_listbox = tk.Listbox(root, width=70, height=25)
        self.task_listbox.pack(pady=10)

        # Entry fields
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack()
        self.name_entry.insert(0, "Task Name")

        self.due_date_entry = tk.Entry(root, width=50)
        self.due_date_entry.pack()
        self.due_date_entry.insert(0, "Due Date (YYYY-MM-DD)")

        self.priority_entry = tk.Entry(root, width=50)
        self.priority_entry.pack()
        self.priority_entry.insert(0, "Priority (Low, Medium, High)")

        # Buttons
        tk.Button(root, text="Add Task", fg="black", bg="green",command=self.addTask).pack(pady=5)
        tk.Button(root, text="Delete Task", fg="black", bg="red",command=self.deleteTask).pack(pady=5)
        tk.Button(root, text="Edit Task", fg="black", bg="white", command=self.editTask).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def file_handling(self):
        with open('Tasks' ,'a') as fileobject:
            for ListItem in self.task_listbox :
                fileobject.write(str(ListItem)+':')
            fileobject.write('\n')
        return

    def show_popup(self, message):
        # Create a new window (popup)
        popup = tk.Toplevel(self.root)
        popup.title("Error")
        popup.geometry("300x150")
        popup.resizable(False, False)

    def addTask(self):
        #convert the input into list
        self.TaskDescription =self.name_entry.get().strip()
        self.Due_Date=self.due_date_entry.get().strip()
        self.Priority=self.priority_entry.get().strip()
        # Check if all fields are filled
        if not self.TaskDescription or not self.Due_Date or not self.Priority:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        # Validate date format (YYYY-MM-DD)
        date_pattern = r"^\d{4}-\d{2}-\d{2}$"  # Regex for YYYY-MM-DD format
        if not re.match(date_pattern, self.Due_Date):
            messagebox.showerror("Input Error", "Please enter the due date in the correct format (YYYY-MM-DD).")
            return

        # Validate priority value
        if self.Priority not in ["Low", "Medium", "High"]:
            messagebox.showerror("Input Error", "Priority must be 'Low', 'Medium', or 'High'.")
            return

        # If all validations pass, create a new Task object and add to listbox
        new_Task = Task(self.TaskDescription, self.Due_Date, self.Priority)
        self.taskslist.append(new_Task)
        self.task_listbox.insert(tk.END, f"Task: {new_Task.TaskDescription} - Due Time: {new_Task.Due_Date} - Priority: {new_Task.Priority} ")
        print("task added successfully")
        return
    # def listAll(self):
    #     with open('Tasks' ,'r') as fileobject:
    #         data=fileobject.readlines()
    #         for line in data:
    #             print(line, end='')
    #         return

    def deleteTask(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showerror("Selection Error", "Please select a task to delete.")
            return
        confirm=messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected task?")
        if confirm:
            task_to_delete = selected_task_index[0]
            self.taskslist.pop(task_to_delete)
            self.task_listbox.delete(task_to_delete)
            messagebox.showinfo("Task Deleted", "The task has been deleted successfully.")


    def editTask(self):
        selected_task_index = self.task_listbox.curselection()
        if not selected_task_index:
            messagebox.showerror("Selection Error", "Please select a task to edit.")
            return
        edite_task_index = selected_task_index[0]
        selected_task = self.taskslist[edite_task_index]

        #clear Labels index

        self.name_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

        # Insert the selected task's data into the entry fields

        self.name_entry.insert(0, f"{selected_task.TaskDescription}")
        self.due_date_entry.insert(0, f"{selected_task.Due_Date}")
        self.priority_entry.insert(0, f"{selected_task.Priority}")

        def Save_TheTask():
            self.TaskDescription = self.name_entry.get().strip()
            self.Due_Date = self.due_date_entry.get().strip()
            self.Priority = self.priority_entry.get().strip()


            # Check if all fields are filled
            if not self.TaskDescription or not self.Due_Date or not self.Priority:
                messagebox.showerror("Input Error", "All fields are required!")
                return

                # Validate date format (YYYY-MM-DD)
            date_pattern = r"^\d{4}-\d{2}-\d{2}$"  # Regex for YYYY-MM-DD format
            if not re.match(date_pattern, self.Due_Date):
                messagebox.showerror("Input Error", "Please enter the due date in the correct format (YYYY-MM-DD).")
                return

                # Validate priority value
            if self.Priority not in ["Low", "Medium", "High"]:
                messagebox.showerror("Input Error", "Priority must be 'Low', 'Medium', or 'High'.")
                return
            new_Task = Task(self.TaskDescription, self.Due_Date, self.Priority)
            self.taskslist[edite_task_index] = new_Task
            self.task_listbox.delete(edite_task_index)
            self.task_listbox.insert(edite_task_index,
                                         f"Task:{new_Task.TaskDescription} - Due Time: {new_Task.Due_Date} - Priority {new_Task.Priority} ")
            messagebox.showinfo("Task Edited", "The task has been edited successfully.")

        save_button = tk.Button(self.root, text="Save Edit", command=Save_TheTask, fg="black", bg="blue")
        save_button.pack(pady=5)


        # choice='task 3'#input("Please Enter Task Name : ")
        # with open('Tasks' ,'r') as fileobject:
        #     data=fileobject.readlines()
        #     for line in data:
        #         item=line.split(':',3)
        #         if item[0] == choice:
        #             data.remove(line)
        #             Task.file_handling(self,data)
        #             print("task deleted successfully")
        #             break
        #     print("task Not Found")



    # def UpdateTask(self):
    #     choice='task 9'#input("Please Enter Task Name : ")
    #     with open('Tasks' ,'r') as fileobject:
    #         data=fileobject.readlines()
    #         for line in data:
    #             item=line.split(':',3)
    #             if item[0] == choice:
    #                 data.remove(line)
    #                 ToDoList.file_handling(self,data)
    #                 break






# for num in range(1,11):
#     task1 = Task(f'task {num}',num,num)
#     Task.addTask(task1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
# Task.listAll(task1)
# task1 = Task("task 3",6,6)
# Task.deleteTask(task1)










