#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a non-negative integer n recursively.

    Parameters:
        n (int): a non-negative integer whose factorial is to be calculated.

    Returns:
        int: the factorial of n (n!), defined as:
            - factorial(0) = 1
            - factorial(n) = n * factorial(n-1) for n > 0

    Example:
        factorial(5) -> 120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
