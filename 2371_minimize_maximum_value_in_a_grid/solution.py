# LeetCode 2371 - Minimize Maximum Value in a Grid
# https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append((grid[i][j], i, j))
        arr.sort()
        row_max = [0] * m
        col_max = [0] * n
        ans = [[0] * n for _ in range(m)]
        for _, i, j in arr:
            val = max(row_max[i], col_max[j]) + 1
            ans[i][j] = val
            row_max[i] = val
            col_max[j] = val
        return ans
