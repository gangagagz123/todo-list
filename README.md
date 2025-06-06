# 📝 To-Do List App

A simple and lightweight **command-line To-Do list application** built using **Python** and **SQLite**.  
This app allows users to manage tasks with features like adding, viewing, marking as completed, and deleting tasks — all stored in a local database.

---

## 📌 Features

-  Add tasks with a due date and priority  
-  View all tasks, sorted by completion and priority  
-  Mark tasks as completed  
-  Delete tasks  
- Stores tasks locally using SQLite database  

---

## 🛠️ Technologies Used

- **Python 3**
- **SQLite3** (Python’s built-in database module)

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/todo-list-cli.git
   cd todo-list-cli
2  **Run the app:**
   -python todo.py
3.  **First-time setup only:**

Uncomment the line in todo.py that creates the table:
# cursor.execute("CREATE TABLE task(...)")
Run the script once to initialize the database, then comment that line again.

 ## Database design :
 | Column      | Type    | Description                   |
| ----------- | ------- | ----------------------------- |
| `id`        | INTEGER | Primary Key (Auto Increment)  |
| `task`      | TEXT    | Task description              |
| `due_date`  | TEXT    | Due date (YYYY-MM-DD)         |
| `priority`  | TEXT    | Priority: High / Medium / Low |
| `completed` | BOOLEAN | 0 = Pending, 1 = Completed    |

## output :

Welcome to the SQLite To-Do List App

Menu:
1 - Add Task
2 - Display Tasks
3 - Mark Task as Completed
4 - Delete Task
5 - Exit
Select an option: 1
Enter task: Write README
Enter due date (YYYY-MM-DD): 2025-06-10
Enter priority (High / Medium / Low): High
Task added successfully.


