import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("study_tracker.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    description TEXT,
    due_date TEXT,
    completed INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    duration INTEGER,
    date TEXT
)
""")

conn.commit()


# Task functions

def add_task():
    subject = input("Subject: ")
    desc = input("Description: ")
    due = input("Due date (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO tasks (subject, description, due_date) VALUES (?, ?, ?)",
        (subject, desc, due)
    )
    conn.commit()
    print("Task added.")


def view_tasks():
    cursor.execute("SELECT * FROM tasks WHERE completed = 0")
    tasks = cursor.fetchall()

    print("\nPending Tasks:")
    for t in tasks:
        print(f"{t[0]}. [{t[1]}] {t[2]} (Due: {t[3]})")


def complete_task():
    task_id = input("Enter task ID to complete: ")

    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    print("Task completed.")


# Study session functions

def log_session():
    subject = input("Subject: ")
    duration = int(input("Duration (minutes): "))
    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "INSERT INTO sessions (subject, duration, date) VALUES (?, ?, ?)",
        (subject, duration, date)
    )
    conn.commit()
    print("Study session logged.")


# Insights

def show_insights():
    print("\nProductivity Insights:")

    # Total study time
    cursor.execute("SELECT SUM(duration) FROM sessions")
    total = cursor.fetchone()[0] or 0
    print(f"Total study time: {total} minutes")

    # Time per subject
    cursor.execute("""
        SELECT subject, SUM(duration)
        FROM sessions
        GROUP BY subject
    """)

    print("\nTime per subject:")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} minutes")

    # Most studied subject
    cursor.execute("""
        SELECT subject, SUM(duration) as total
        FROM sessions
        GROUP BY subject
        ORDER BY total DESC
        LIMIT 1
    """)

    top = cursor.fetchone()
    if top:
        print(f"\nMost studied subject: {top[0]}")


# Main menu

def menu():
    while True:
        print("\n==== STUDY TRACKER ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Log Study Session")
        print("5. Show Insights")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            log_session()
        elif choice == "5":
            show_insights()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


menu()
conn.close()
