#!/usr/bin/python3
"""
Script calculates the perimeter of an island
"""
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell initially contributes 4 to the perimeter
                perimeter += 4

                # If the cell above is land, subtract 2 (shared edge)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # If the cell to the left is land, subtract 2 (shared edge)
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter

# if __name__ == "__main__":
#     grid = [
#         [0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0]
#     ]
#     print(island_perimeter(grid))
