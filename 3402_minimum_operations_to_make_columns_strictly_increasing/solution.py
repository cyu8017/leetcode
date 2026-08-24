# LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for j in range(n):
            for i in range(1, m):
                if grid[i][j] <= grid[i - 1][j]:
                    need = grid[i - 1][j] + 1
                    ans += need - grid[i][j]
                    grid[i][j] = need
        return ans
