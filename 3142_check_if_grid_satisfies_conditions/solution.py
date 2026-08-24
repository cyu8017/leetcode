# LeetCode 3142 - Check if Grid Satisfies Conditions
# https://leetcode.com/problems/check-if-grid-satisfies-conditions/

from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                if i + 1 < m and x != grid[i + 1][j]:
                    return False
                if j + 1 < n and x == grid[i][j + 1]:
                    return False
        return True
