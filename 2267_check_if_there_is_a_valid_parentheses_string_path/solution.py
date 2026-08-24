# LeetCode 2267 - Check if There Is a Valid Parentheses String Path
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1 or grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False
        vis = set()

        def dfs(r: int, c: int, bal: int) -> bool:
            if r >= m or c >= n:
                return False
            bal += 1 if grid[r][c] == "(" else -1
            if bal < 0:
                return False
            if r == m - 1 and c == n - 1:
                return bal == 0
            k = ((r * n + c) << 10) | bal
            if k in vis:
                return False
            vis.add(k)
            return dfs(r + 1, c, bal) or dfs(r, c + 1, bal)

        return dfs(0, 0, 0)
