# LeetCode 3195 - Find the Minimum Area to Cover All Ones I
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x1, y1 = len(grid), len(grid[0])
        x2, y2 = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x1 = min(x1, i)
                    y1 = min(y1, j)
                    x2 = max(x2, i)
                    y2 = max(y2, j)
        return (x2 - x1 + 1) * (y2 - y1 + 1)
