## Concepts Needed:
<b>1. Greedy Algorithms:</b>

- Understanding how greedy algorithms work and why they are suitable for the coin change problem.
- Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.

<b>2. Dynamic Programming:</b>

- Basic principles of dynamic programming as a method to solve optimization problems.
- The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.

<b>3. Algorithmic Complexity:</b>

- Analyzing the time and space complexity of algorithms.
- Striving for solutions with lower complexity to meet runtime constraints.

<b>4. Problem-Solving Strategies:</b>

- Breaking down the problem into smaller, manageable sub-problems.
- Iterative vs recursive approaches to dynamic programming.

<b>5. Python Programming:</b>

- Manipulating lists and using list comprehensions.
- Implementing functions with efficient looping and conditional statements.

### Resources:
- Python Official Documentation:

  - [More Control Flow Tools (for loops, if statements)](https://docs.python.org/3/tutorial/controlflow.html)

- GeeksforGeeks Articles:

  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

- YouTube Tutorials:

  -[ Dynamic Programming - Coin Change Problem for a visual and step-by-step explanation of the dynamic programming approach.](https://www.youtube.com/watch?v=jgiZlGzXMBw)

## Additional Resources
[Mock Technical Interview](https://www.youtube.com/watch?v=9BSSIsJ-fWg)

## Tasks
<b>0. Change comes from within</b>

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet total
  - If `total` is `0` or less, return `0`
  - If `total` cannot be met by any number of coins you have, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

```Bash
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$```

```Bash
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```