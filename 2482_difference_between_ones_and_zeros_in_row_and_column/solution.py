# LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j])
        return ans
