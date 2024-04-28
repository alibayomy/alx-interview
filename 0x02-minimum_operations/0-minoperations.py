#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """calculates the fewest number of operations needed to result
        in exactly n H characters in the file."""
    if n in [0, 1]:
        return 0
    for num in range(2, n+1):
        if n % num == 0:
            return num + minOperations(int(n/num))
    return n
