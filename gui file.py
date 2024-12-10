import tkinter as tk
from MainFile import *
class ToDoApp:
    def __init__(self,root):
        self.root = root
        self.root.title("To-Do List App")

        # Task list display
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Entry fields
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack()
        self.name_entry.insert(0, "Task Name")

        self.due_date_entry = tk.Entry(root, width=40)
        self.due_date_entry.pack()
        self.due_date_entry.insert(0, "Due Date (YYYY-MM-DD)")

        self.priority_entry = tk.Entry(root, width=40)
        self.priority_entry.pack()
        self.priority_entry.insert(0, "Priority (Low, Medium, High)")

        # Buttons
        tk.Button(root, text="Add Task",fg="green",bg="yellow").pack(pady=5)
        tk.Button(root, text="Delete Task",fg="black",bg="red").pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
    # Main window setup

# myframe =Tk()
# my_button=Button(myframe,text="click me ")


