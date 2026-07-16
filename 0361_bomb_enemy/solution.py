# LeetCode 0361 - Bomb Enemy
# https://leetcode.com/problems/bomb-enemy/

from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        row_hits = [[0] * cols for _ in range(rows)]
        col_hits = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            count = 0
            for col in range(cols):
                if grid[row][col] == "W":
                    count = 0
                elif grid[row][col] == "E":
                    count += 1
                else:
                    row_hits[row][col] = count
            count = 0
            for col in range(cols - 1, -1, -1):
                if grid[row][col] == "W":
                    count = 0
                elif grid[row][col] == "E":
                    count += 1
                else:
                    row_hits[row][col] += count

        for col in range(cols):
            count = 0
            for row in range(rows):
                if grid[row][col] == "W":
                    count = 0
                elif grid[row][col] == "E":
                    count += 1
                else:
                    col_hits[row][col] = count
            count = 0
            for row in range(rows - 1, -1, -1):
                if grid[row][col] == "W":
                    count = 0
                elif grid[row][col] == "E":
                    count += 1
                else:
                    col_hits[row][col] += count

        return max(row_hits[row][col] + col_hits[row][col] for row in range(rows) for col in range(cols))
