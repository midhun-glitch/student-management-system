import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    email TEXT
)
""")
conn.commit()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    email = input("Enter email: ")

    cursor.execute(
        "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
        (name, age, course, email)
    )
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print(" No students found.")
        return

    print("\nID | Name | Age | Course | Email")
    print("-" * 40)
    for row in rows:
        print(row)

def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("New name: ")
    age = int(input("New age: "))
    course = input("New course: ")
    email = input("New email: ")

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=?, email=? WHERE id=?",
        (name, age, course, email, student_id)
    )
    conn.commit()
    print(" Student updated!")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print(" Student deleted!")

def menu():
    while True:
        print("""
======== Student Management System ========
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
===========================================
""")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!")

menu()
conn.close()
