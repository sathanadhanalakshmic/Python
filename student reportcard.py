students=[]

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    subjects = ["Maths", "Chemistry", "English", "Physics", "Python"]
    marks = {}
    total = 0
    passed = True

    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks[subject] = mark
        total += mark
        if mark < 35:
            passed = False

    percentage = total / len(subjects)
    status = "Pass" if passed else "Fail"

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "status": status,
        "rank": "-"
    }

    students.append(student)

def assign_ranks():
    passed_students = [s for s in students if s["status"] == "Pass"]
    passed_students.sort(key=lambda s: s["total"], reverse=True)
    for i, s in enumerate(passed_students):
        s["rank"] = i + 1
    for s in students:
        if s["status"] == "Fail":
            s["rank"] = "-"

def display_all():
    assign_ranks()
    for s in students:
        print("\n--- Report Card ---")
        print("Roll No:", s["roll_no"])
        print("Name:", s["name"])
        for subject, mark in s["marks"].items():
            print(f"{subject}: {mark}")
        print("Total Marks:", s["total"])
        print("Percentage:", round(s["percentage"], 2))
        print("Status:", s["status"])
        print("Rank:", s["rank"])

def display_by_roll_no():
    assign_ranks()
    roll = input("Enter Roll Number to search: ")
    found = False
    for s in students:
        if s["roll_no"] == roll:
            print("\n--- Report Card ---")
            print("Roll No:", s["roll_no"])
            print("Name:", s["name"])
            for subject, mark in s["marks"].items():
                print(f"{subject}: {mark}")
            print("Total Marks:", s["total"])
            print("Percentage:", round(s["percentage"], 2))
            print("Status:", s["status"])
            print("Rank:", s["rank"])
            found = True
            break
    if not found:
        print("Student not found.")

# New function to display roll no, percentage, pass/fail for all students
def display_percentage_status():
    if not students:
        print("No students added yet.")
        return
    print("\nRoll No | Percentage | Status")
    print("----------------------------")
    for s in students:
        print(f"{s['roll_no']} | {round(s['percentage'], 2)}% | {s['status']}")

def main():
    while True:
        print("\n1. Add Student")
        print("2. Display All Report Cards")
        print("3. Display Report Card by Roll Number")
        print("4. Display Percentage and Pass/Fail of All Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all()
        elif choice == "3":
            display_by_roll_no()
        elif choice == "4":
            display_percentage_status()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

main()
