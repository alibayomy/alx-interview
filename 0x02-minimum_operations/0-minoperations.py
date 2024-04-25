#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """calculates the fewest number of operations needed to result
        in exactly n H characters in the file."""
    operations = 0
    if n == 0:
        return 0
    if n == 3:
        return 3
    if n == 2:
        return 2
    if n % 3 == 0:
        total_operations = n // 3
        operations = 3 + 2
        for _ in range(0, total_operations - 2):
            operations += 1
    elif n % 2 == 0:
        total_operations = n // 2
        operations = 2 + 2
        for _ in range(0, total_operations - 2):
            operations += 1
    return operations
