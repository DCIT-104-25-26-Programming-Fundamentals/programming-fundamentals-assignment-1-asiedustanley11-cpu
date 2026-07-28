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

def show_menu():
    """
    Print the main menu.
    """
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
 
 
def calculate_average(scores):
    """
    Return the average of a list of scores, rounded to 2 decimal places.
    Returns 0 if the list is empty (avoids dividing by zero).
    """
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)
 
 
def add_student(students):
    """
    Prompt the user for a student's name, ID, and scores, then add the
    new student record (a dictionary) to the students list.
    """
    name = input("Student name: ").strip()
 
    id_input = input("Student ID: ").strip()
    try:
        student_id = int(id_input)
    except ValueError:
        print("Invalid ID. Student was not added.")
        return
 
    count_input = input("How many scores? ").strip()
    try:
        num_scores = int(count_input)
        if num_scores < 0:
            raise ValueError
    except ValueError:
        print("Invalid number of scores. Student was not added.")
        return
 
    scores = []
    for i in range(1, num_scores + 1):
        score_input = input(f"Enter score {i}: ").strip()
        try:
            score = float(score_input)
        except ValueError:
            print("Invalid score entered. Student was not added.")
            return
        scores.append(score)
 
    # Build the student record as a dictionary and add it to the list.
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
 
    print(f'Student "{name}" added successfully.')
 
 
def display_all_students(students):
    """
    Print a formatted table of all students: name, ID, scores, and
    average score.
    """
    if not students:
        print("No students have been added yet.")
        return
 
    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)
 
    for student in students:
        scores_text = ", ".join(str(int(s)) if s == int(s) else str(s)
                                 for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}"
              f"{scores_text:<15}{average:<10}")
 
    print("-" * 50)
 
 
def find_student_by_id(students, student_id):
    """
    Search the students list for a record matching the given ID.
    Return the matching dictionary, or None if not found.
    """
    for student in students:
        if student["id"] == student_id:
            return student
    return None
 
 
def show_average_for_student(students):
    """
    Ask for a student ID, look up that student, and display their
    average score. Prints an error message if the ID is not found.
    """
    id_input = input("Enter student ID: ").strip()
 
    try:
        student_id = int(id_input)
    except ValueError:
        print("Invalid ID format.")
        return
 
    student = find_student_by_id(students, student_id)
 
    if student is None:
        print(f"Error: no student found with ID {student_id}.")
        return
 
    average = calculate_average(student["scores"])
    print(f"{student['name']}'s average score: {average}")
 
 
def main():
    students = []  # list of dictionaries, one per student
 
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
 
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            show_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
 
        print()  # blank line for readability before the menu repeats
 
 
if __name__ == "__main__":
    main()