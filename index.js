 import json
import os

FILE = "students.json"

def load_students():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    students = load_students()

    name = input("Enter name: ").strip()
    roll = input("Enter roll number: ").strip()

    try:
        marks = int(input("Enter marks: "))
    except ValueError:
        print("❌ Marks must be a number")
        return

    for s in students:
        if s["roll"] == roll:
            print("❌ Roll number already exists")
            return

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    save_students(students)
    print("✅ Student added successfully")

def view_students():
    students = load_students()

    if not students:
        print("📭 No students found")
        return

    print("\n📋 Student List")
    print("-" * 30)
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Roll: {s['roll']}")
        print(f"Marks: {s['marks']}")
        print("-" * 30)

def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    students = load_students()

    new_students = [s for s in students if s["roll"] != roll]

    if len(new_students) == len(students):
        print("❌ Student not found")
        return

    save_students(new_students)
    print("🗑️ Student deleted successfully")

def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Choose option (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice")

menu()
