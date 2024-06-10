# 0x09. Island Perimeter

## Concepts Needed:
<b>1. 2D Arrays (Matrices):</b>

- Accessing and iterating over elements in a 2D array.
- Understanding how to navigate through adjacent cells (horizontally and vertically).

<b>2. Conditional Logic:</b>

- Applying conditions to determine whether a cell contributes to the perimeter of the island.
<b>3.Counting Techniques:</b>

- Developing a method to count the edges that contribute to the island’s perimeter.

<b>4. Problem-Solving Strategies:</b>

- Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

<b>5. Python Programming:</b>

- Nested loops for iterating over grid cells.
- Conditional statements to check the status of adjacent cells.

## Resources:
<b>- Python Official Documentation:</b>

- [Nested Lists: Understanding how to work with lists within lists in Python.](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)

<b>- GeeksforGeeks Articles:</b>

- [Python Multi-dimensional Arrays: A guide to working with 2D arrays in Python effectively.](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)

<b>- TutorialsPoint:</b>

- [Python Lists: Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.](https://www.tutorialspoint.com/python/python_lists.htm)

<b>- YouTube Tutorials:</b>

- [Python 2D arrays and lists](https://www.youtube.com/watch?v=aNzepGawwCI)

## Additional Resources
[Mock Technical Interviews](https://www.youtube.com/watch?v=fFgEM6CMQc4)

##2 Tasks
<b>0. Island Perimeter</b>

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
  - 0 represents water
  - 1 represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```Bash
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$ ```