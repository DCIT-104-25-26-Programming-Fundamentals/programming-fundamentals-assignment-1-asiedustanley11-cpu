# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_table(number):
    """
    Print the multiplication table for the given number, from 1 to 12.
    """
    print(f"Multiplication Table for {number}:")
 
    # Loop through multipliers 1 through 12 (range(1, 13) stops before 13).
    for multiplier in range(1, 13):
        product = number * multiplier
        # :<2 left-aligns the multiplier in a 2-character-wide field so
        # results line up neatly even once the multiplier reaches 2 digits.
        print(f"{number} x {multiplier:<2} = {product}")
 
 
# -----------------------------------------------------------------------------
# PART B — Tables from 1 to N
# -----------------------------------------------------------------------------
def print_tables_up_to(n):
    """
    Print the full multiplication table (1-12) for every number from
    1 to n, separated by a divider line.
    """
    for number in range(1, n + 1):
        print_table(number)
 
        # Add a separator line after each table except the very last one.
        if number != n:
            print("-" * 27)
 
 
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
    # PART A — Single table
    # -------------------------------------------------------------------
    number = get_positive_int("Enter a number: ")
 
    if number is None:
        print("Error: please enter a positive integer.")
        return
 
    print_table(number)
 
    # -------------------------------------------------------------------
    # PART B — Tables from 1 to N
    # -------------------------------------------------------------------
    print()  # blank line to separate Part A output from Part B prompt
    n = get_positive_int("Enter N to print tables from 1 to N: ")
 
    if n is None:
        print("Error: please enter a positive integer.")
        return
 
    print()
    print_tables_up_to(n)
 
 
if __name__ == "__main__":
    main()