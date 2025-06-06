# sql table creation
import sqlite3
conn=sqlite3.connect('todo.db')
cursor=conn.cursor()
#
# cursor.execute("CREATE TABLE task(id INTEGER PRIMARY KEY,task TEXT NOT NULL ,due_date TEXT, priority TEXT , completed BOOLEAN DEFAULT 0) ")
# conn.commit()




# Function to add a task
def add_task():
    task = input("Enter task: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (High / Medium / Low): ").strip().capitalize()

    if task:
        cursor.execute("INSERT INTO task (task, due_date, priority) VALUES (?, ?, ?)",
                       (task, due_date, priority))
        conn.commit()
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

# Function to display all tasks
def display_tasks():
    cursor.execute("SELECT id, task, due_date, priority, completed FROM task ORDER BY completed, priority")
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks in your list.")
        return

    print("\n------ TO-DO TASKS ------")
    for task in tasks:
        status = "Completed" if task[4] else "Pending"
        print(f"{task[0]}. {task[1]} | Due: {task[2]} | Priority: {task[3]} | Status: {status}")
    print("--------------------------")

# Function to mark a task as completed
def mark_task_completed():
    task_id = input("Enter task ID to mark as completed: ").strip()
    if task_id.isdigit():
        cursor.execute("UPDATE task SET completed = 1 WHERE id = ?", (int(task_id),))
        conn.commit()
        print("Task marked as completed.")
    else:
        print("Invalid input. Please enter a valid task ID.")

# Function to delete a task
def delete_task():
    task_id = input("Enter task ID to delete: ").strip()
    if task_id.isdigit():
        cursor.execute("DELETE FROM task WHERE id = ?", (int(task_id),))
        conn.commit()
        print("Task deleted successfully.")
    else:
        print("Invalid input. Please enter a valid task ID.")

# Main function
def main():
    print("Welcome to the SQLite To-Do List App")

    while True:
        print("\nMenu:")
        print("1 - Add Task")
        print("2 - Display Tasks")
        print("3 - Mark Task as Completed")
        print("4 - Delete Task")
        print("5 - Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

    conn.close()

# Start the program
if __name__ == "__main__":
    main()