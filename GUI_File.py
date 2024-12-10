import tkinter as tk

class Task:
    def __init__(self, task_description, due_date, priority):
        self.task_description = task_description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.task_description}:{self.due_date}:{self.priority}"


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []  # List of Task objects

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
        tk.Button(root, text="Add Task", fg="green", bg="yellow", command=self.add_task).pack(pady=5)
        tk.Button(root, text="Delete Task", fg="black", bg="red", command=self.delete_task).pack(pady=5)
        tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    def save_tasks_to_file(self):
        with open('Tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(str(task) + '\n')

    def load_tasks_from_file(self):
        try:
            with open('Tasks.txt', 'r') as file:
                self.tasks = []
                for line in file:
                    task_description, due_date, priority = line.strip().split(':')
                    self.tasks.append(Task(task_description, due_date, priority))
                    self.task_listbox.insert(tk.END, task_description)
        except FileNotFoundError:
            pass

    def add_task(self):
        task_description = self.name_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if task_description and due_date and priority:
            new_task = Task(task_description, due_date, priority)
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, task_description)
            self.save_tasks_to_file()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
            self.save_tasks_to_file()
        else:
            print("No task selected for deletion")


# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    app.load_tasks_from_file()
    root.mainloop()
