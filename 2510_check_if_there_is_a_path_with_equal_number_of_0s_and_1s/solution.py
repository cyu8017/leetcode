# LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
# https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

from typing import List


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        target = (m + n - 1) // 2
        memo = {}

        def dfs(r: int, c: int, bal: int) -> bool:
            if r >= m or c >= n:
                return False
            bal += grid[r][c]
            if bal > target or bal + (m - 1 - r) + (n - 1 - c) < target:
                return False
            if r == m - 1 and c == n - 1:
                return bal == target
            key = (r, c, bal)
            if key in memo:
                return memo[key]
            ok = dfs(r + 1, c, bal) or dfs(r, c + 1, bal)
            memo[key] = ok
            return ok

        return dfs(0, 0, 0)
