#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of n.  Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Check if there's at least one argument
        try:
            number = int(sys.argv[1])
            if number < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                f = factorial(number)
                print(f)
        except ValueError:
            print("Error: Please provide a valid integer argument.")
    else:
        print("Error: Please provide an integer argument.")
