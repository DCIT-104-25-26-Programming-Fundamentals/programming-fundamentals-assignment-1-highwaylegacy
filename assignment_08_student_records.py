# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

"""Student Record Management System — list of dictionaries, loops and functions."""


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimals."""
    if not scores:
        return 0.0
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def find_student(students, student_id):
    """Return the student dictionary with the given ID, or None."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def format_score(value):
    """Show 85 instead of 85.0 for whole numbers."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def read_int(prompt):
    """Read a whole number, re-prompting until valid."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


# -----------------------------------------------------------------------------
# Feature 1 — Add a student
# -----------------------------------------------------------------------------
def add_student(students):
    """Collect a student's name, ID and scores, then store the record."""
    name = input("Student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    student_id = read_int("Student ID: ")
    if find_student(students, student_id) is not None:
        print(f"Error: A student with ID {student_id} already exists.")
        return

    while True:
        count = read_int("How many scores? ")
        if count > 0:
            break
        print("  The number of scores must be a positive integer.")

    scores = []
    for i in range(1, count + 1):
        while True:
            try:
                score = float(input(f"Enter score {i}: "))
            except ValueError:
                print("  Invalid input. Please enter a number.")
                continue
            if score < 0 or score > 100:
                print("  Score must be between 0 and 100.")
                continue
            scores.append(score)
            break

    students.append({"name": name, "id": student_id, "scores": scores})
    print(f'Student "{name}" added successfully.')


# -----------------------------------------------------------------------------
# Feature 2 — Display all students
# -----------------------------------------------------------------------------
def display_students(students):
    """Print every student record in an aligned table."""
    if not students:
        print("No students have been added yet.")
        return

    rows = []
    for student in students:
        scores_text = ", ".join(format_score(s) for s in student["scores"])
        rows.append([
            student["name"],
            str(student["id"]),
            scores_text,
            f"{calculate_average(student['scores']):.2f}",
        ])

    headers = ["Name", "ID", "Scores", "Average"]
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(cell) > widths[i]:
                widths[i] = len(cell)

    line = "-" * (sum(widths) + 3 * (len(widths) - 1))
    print(line)
    print("   ".join(headers[i].ljust(widths[i]) for i in range(len(headers))))
    print(line)
    for row in rows:
        print("   ".join(row[i].ljust(widths[i]) for i in range(len(row))))
    print(line)


# -----------------------------------------------------------------------------
# Feature 3 — Average for a specific student
# -----------------------------------------------------------------------------
def student_average(students):
    """Look up a student by ID and show their average score."""
    if not students:
        print("No students have been added yet.")
        return

    student_id = read_int("Enter student ID: ")
    student = find_student(students, student_id)
    if student is None:
        print(f"Error: No student found with ID {student_id}.")
        return

    average = calculate_average(student["scores"])
    print(f"{student['name']}'s average score: {average:.2f}")


# -----------------------------------------------------------------------------
# Menu
# -----------------------------------------------------------------------------
def display_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()