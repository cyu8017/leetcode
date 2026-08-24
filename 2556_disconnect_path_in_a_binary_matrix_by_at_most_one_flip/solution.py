# LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> bool:
            if r == m - 1 and c == n - 1:
                return True
            if r >= m or c >= n or grid[r][c] == 0:
                return False
            if not (r == 0 and c == 0):
                grid[r][c] = 0
            return dfs(r + 1, c) or dfs(r, c + 1)

        if not dfs(0, 0):
            return True
        grid[0][0] = 1
        return not dfs(0, 0)
