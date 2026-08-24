# LeetCode 2128 - Remove All Ones With Row and Column Flips
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

from typing import List
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            same = grid[i][0] == grid[0][0]
            for j in range(n):
                if (grid[i][j] == grid[0][j]) != same:
                    return False
        return True
