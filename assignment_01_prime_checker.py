def is_prime(n):
    """
    Return True if n is a prime number, False otherwise.

    A prime number is a whole number greater than 1 that has no
    divisors other than 1 and itself.
    """
    # Numbers less than 2 are never prime
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # No other even number can be prime
    if n % 2 == 0:
        return False

    # Check odd divisors up to the square root of n.
    # If n has a factor larger than its square root, it must also
    # have a corresponding factor smaller than the square root,
    # so checking up to sqrt(n) is enough.
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2

    return True


def main():
    # Get input from the user
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid whole number.")
        return

    # Call the function and print the result
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")


if __name__ == "__main__":
    main()
