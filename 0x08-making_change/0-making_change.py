#!/usr/bin/python3
"""
Python script to solve a dynamic programming problem
"""


def makeChange(coins, total):
    """
    Function to calculate the minimum number of coins needed to make a
    given total.

    This function uses a dynamic programming approach to solve the problem.
    It creates a list dp where dp[i] represents the minimum number
    of coins needed to make a total of i. The function iterates over each coin,
    and for each coin it iterates over each total from 0 to the given total.
    If the current coin is less than or equal to the current total,
    it updates dp[i] to be the minimum of the current value of dp[i] and
    dp[i-coin] + 1.

    Parameters:
    coins (list of int): A list of integers representing the
    denominations of the coins.
    total (int): The total amount for which we want to make change.

    Returns:
    int: The minimum number of coins needed to make the given total.
    If it's not possible to make the total
    with the given coins, it returns -1.
    """
    if not coins:
        return -1
    if total <= 0:
        return 0
    if total < min(coins):
        return -1

    dp = [total+1 for i in range(total+1)]
    dp[0] = 0

    for i in range(total+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i-coin]+1, dp[i])
    return dp[-1]
