# LeetCode 2596 - Check Knight Tour Configuration
# https://leetcode.com/problems/check-knight-tour-configuration/

from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        pos = [None] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = [i, j]
        dirs = [
            [1, 2], [1, -2], [-1, 2], [-1, -2],
            [2, 1], [2, -1], [-2, 1], [-2, -1],
        ]
        for v in range(n * n - 1):
            r, c = pos[v]
            ok = False
            for dr, dc in dirs:
                if r + dr == pos[v + 1][0] and c + dc == pos[v + 1][1]:
                    ok = True
                    break
            if not ok:
                return False
        return True
