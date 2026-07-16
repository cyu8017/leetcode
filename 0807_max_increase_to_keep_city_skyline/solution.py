# LeetCode 0807 - Max Increase to Keep City Skyline
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        return sum(
            min(row_max[r], col_max[c]) - grid[r][c]
            for r in range(len(grid))
            for c in range(len(grid[0]))
        )
