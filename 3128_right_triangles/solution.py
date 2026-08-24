# LeetCode 3128 - Right Triangles
# https://leetcode.com/problems/right-triangles/

from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += (rows[i] - 1) * (cols[j] - 1)
        return ans
