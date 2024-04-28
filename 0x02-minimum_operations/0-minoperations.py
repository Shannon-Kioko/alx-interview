#!/usr/bin/python3
"""
This script computes the minimum number of operations
required to copy all and paste ceratin number of 'H' characters
"""


def minOperations(n):
    """
    Method for compute the minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """

    if n <= 1:
        return 0

    divisor = 2
    number_of_operations = 0

    while n > 1:
        if n % divisor == 0:
            n /= divisor
            number_of_operations += divisor
        else:
            divisor += 1

    return number_of_operations
