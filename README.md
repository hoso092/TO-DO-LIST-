# To-Do List Application

## Overview

This project is a **To-Do List Application** built using Python and the Tkinter library. It allows users to manage their daily tasks efficiently with features such as adding, editing, deleting, and saving tasks.

## Features

1. **Add Tasks**: Add new tasks with a description, due date, and priority level.
2. **Edit Tasks**: Modify details of existing tasks.
3. **Delete Tasks**: Remove tasks from the list.
4. **Save Tasks**: Save the list of tasks to a text file for future reference.
5. **Exit Application**: Save the current session's tasks and exit the program.

## Requirements

- Python 3.x
- Tkinter (built-in with Python)
- `re` module (built-in with Python)

## File Structure

- `Task`: A class representing an individual task.
- `ToDoApp`: A class inheriting from `Task` that manages the application logic and GUI.
- `Tasks.txt`: A file to store tasks persistently.

## Setup Instructions

1. Ensure Python 3 is installed on your system.
2. Save the script to a file (e.g., `todo_app.py`).
3. Run the script using the following command:
   ```bash
   python todo_app.py
   ```

## Usage

### Adding a Task

1. Enter the task details in the respective entry fields:
   - **Task Name**: A brief description of the task.
   - **Due Date**: The deadline in `YYYY-MM-DD` format.
   - **Priority**: The importance of the task (Low, Medium, High).
2. Click on the **Add Task** button to add the task to the list.

### Editing a Task

1. Select a task from the list.
2. Click on the **Edit Task** button.
3. Modify the task details in the entry fields.
4. Click the **Save Edit** button to update the task.

### Deleting a Task

1. Select a task from the list.
2. Click on the **Delete Task** button.
3. Confirm the deletion in the popup dialog.

### Saving and Exiting

1. Click on the **Exit** button to save all tasks to `Tasks.txt` and close the application.

## Code Structure

### Classes

#### 1. `Task`

- Represents an individual task with the following attributes:
  - `TaskDescription` (str): Description of the task.
  - `Due_Date` (str): Due date in `YYYY-MM-DD` format.
  - `Priority` (str): Task priority (Low, Medium, High).

#### 2. `ToDoApp`

- Inherits from `Task` and handles the application logic and user interface.

### Key Methods

1. **`addTask()`**: Adds a new task to the list after validation.
2. **`deleteTask()`**: Deletes the selected task from the list.
3. **`editTask()`**: Edits the selected task's details.
4. **`save_and_exit()`**: Saves tasks to `Tasks.txt` and exits the application.
5. **`Store_in_txt()`**: Writes tasks to a text file for persistence.

## Task Validation

- **Due Date Format**: Ensures the date follows the `YYYY-MM-DD` format using regex.
- **Priority**: Accepts only "Low," "Medium," or "High" as valid values.
- **Mandatory Fields**: All fields are required to proceed.

## Example Output in `Tasks.txt`

```txt
Task: Finish project report - Due Time: 2024-12-20 - Priority: High
Task: Grocery shopping - Due Time: 2024-12-21 - Priority: Medium
END_OF_SESSION
```

## Acknowledgments

- **Tkinter**: For the GUI components.
- **Regex Module**: For validating input formats.

