# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(a, b):
    return a + b
 
 
def subtract(a, b):
    return a - b
 
 
def multiply(a, b):
    return a * b
 
 
def divide(a, b):
    """
    Return a / b rounded to 2 decimal places.
    Raises ZeroDivisionError if b is 0, so the caller can handle it.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)
 
 
def modulus(a, b):
    """
    Return the remainder of a / b.
    Raises ZeroDivisionError if b is 0, so the caller can handle it.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a % b
 
 
def exponentiate(a, b):
    return a ** b
 
 
def show_menu():
    """
    Print the calculator's main menu.
    """
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
 
 
def get_number(prompt):
    """
    Ask the user for a number, returning None if the input is invalid.
    """
    user_input = input(prompt)
    try:
        return float(user_input)
    except ValueError:
        return None
 
 
def main():
    # Maps each menu choice to the matching operation's symbol and function.
    # Keeping this table here (rather than a long if/elif chain) makes it
    # easy to see, at a glance, which choice goes with which operation.
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }
 
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ").strip()
 
        if choice == "7":
            print("Goodbye!")
            break
 
        if choice not in operations:
            print("Invalid choice. Please select a number from 1 to 7.")
            print()
            continue
 
        symbol, operation_func = operations[choice]
 
        first_number = get_number("Enter first number : ")
        if first_number is None:
            print("Invalid number entered.")
            print()
            continue
 
        second_number = get_number("Enter second number: ")
        if second_number is None:
            print("Invalid number entered.")
            print()
            continue
 
        try:
            result = operation_func(first_number, second_number)
        except ZeroDivisionError as error:
            print(f"Error: {error}")
            print()
            continue
 
        # Format numbers without a trailing ".0" for whole-number inputs,
        # so "10 + 3 = 13" looks cleaner than "10.0 + 3.0 = 13.0".
        def fmt(n):
            return str(int(n)) if n == int(n) else str(n)
 
        print(f"Result: {fmt(first_number)} {symbol} {fmt(second_number)} = {fmt(result)}")
        print()
 
 
if __name__ == "__main__":
    main()