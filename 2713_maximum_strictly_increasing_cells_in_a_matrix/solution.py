# LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

from typing import List


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((mat[i][j], i, j))
        cells.sort()
        row_max = [0] * m
        col_max = [0] * n
        dp = [[0] * n for _ in range(m)]
        ans = 0
        i = 0
        while i < len(cells):
            j = i
            while j < len(cells) and cells[j][0] == cells[i][0]:
                j += 1
            buf = []
            for k in range(i, j):
                r, c = cells[k][1], cells[k][2]
                best = max(row_max[r], col_max[c])
                dp[r][c] = best + 1
                ans = max(ans, dp[r][c])
                buf.append((r, c, dp[r][c]))
            for r, c, v in buf:
                row_max[r] = max(row_max[r], v)
                col_max[c] = max(col_max[c], v)
            i = j
        return ans
