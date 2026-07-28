# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def fibonacci_terms(n):
    """
    Return a list containing the first n terms of the Fibonacci sequence.
 
    Assumes n is already a positive integer (validation happens in main()).
    """
    sequence = []
    a, b = 0, 1
 
    # Build the sequence one term at a time using a loop (no recursion).
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # slide the two "tracking" numbers forward
 
    return sequence
 
 
# -----------------------------------------------------------------------------
# PART B — Check Membership
# -----------------------------------------------------------------------------
def is_fibonacci_number(number):
    """
    Return True if the given number appears in the Fibonacci sequence,
    False otherwise.
    """
    # Negative numbers are never part of the sequence.
    if number < 0:
        return False
 
    # Generate Fibonacci numbers with a loop, stopping once we reach
    # or pass the target number.
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
 
    # After the loop, "a" is either equal to the number (found it)
    # or has jumped past it (not a Fibonacci number).
    return a == number
 
 
def get_positive_int(prompt):
    """
    Ask the user for a positive whole number, returning None if the
    input is invalid (not a whole number, or not positive).
    """
    user_input = input(prompt)
 
    try:
        value = int(user_input)
    except ValueError:
        return None
 
    if value <= 0:
        return None
 
    return value
 
 
def main():
    # -------------------------------------------------------------------
    # PART A — Print the first N terms
    # -------------------------------------------------------------------
    n = get_positive_int("How many terms? ")
 
    if n is None:
        print("Error: N must be a positive integer.")
    else:
        sequence = fibonacci_terms(n)
        # Convert each number to a string, then join them with spaces.
        sequence_text = " ".join(str(term) for term in sequence)
        print(f"Fibonacci sequence: {sequence_text}")
 
    # -------------------------------------------------------------------
    # PART B — Check if a number belongs to the sequence
    # -------------------------------------------------------------------
    check_input = input("Enter a number to check: ")
 
    try:
        number = int(check_input)
    except ValueError:
        print("Please enter a valid whole number.")
        return
 
    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")
 
 
if __name__ == "__main__":
    main()