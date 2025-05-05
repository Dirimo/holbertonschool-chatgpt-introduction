#!/usr/bin/python3

import sys

def factorial(n):
    result = 1
    if n == 1
        return 1
    while n > 1:
        result *= n
        n -= 1 # Decrement n in each iteration
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            f = factorial(num)
            print (f)
        except ValueError:
            print("Error : Please provide a valide integer argument.")
    else:
        print("Error : Please provide an integer argument.")
