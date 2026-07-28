# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter student score (0-100): 85
#   Grade: A
#
#   Enter student score (0-100): 73
#   Grade: B
#
#   Enter student score (0-100): 45
#   Grade: F
#
#   Enter student score (0-100): 110
#   Error: Score must be between 0 and 100.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST use functions (see scaffold below).
# - Validate that the score is within the range 0–100 inside get_grade().
#   If it is not, return None and let main() print the error message.
# - Use if / elif / else to determine the grade.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_grade(score):
    """
    Return the letter grade (A, B, C, D, or F) for a given score.
 
    If the score is outside the valid range of 0-100, return None
    so that main() can print an appropriate error message.
    """
    # Validate the score is within the allowed range
    if score < 0 or score > 100:
        return None
 
    # Determine the letter grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
 
    return grade
 
 
def main():
    # Get input from the user
    user_input = input("Enter student score (0-100): ")
 
    try:
        score = int(user_input)
    except ValueError:
        print("Please enter a valid whole number.")
        return
 
    # Call the function and print the result
    grade = get_grade(score)
 
    if grade is None:
        print("Error: Score must be between 0 and 100.")
    else:
        print(f"Grade: {grade}")
 
 
if __name__ == "__main__":
    main()