# LeetCode 2174 - Remove All Ones With Row and Column Flips II
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

from typing import List
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ones = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.append([i, j])
        if len(ones) == 0:
            return 0
        ans = m + n
        def dfs(idx, flips):
            nonlocal ans
            if flips >= ans:
                return
            while idx < len(ones) and grid[ones[idx][0]][ones[idx][1]] == 0:
                idx += 1
            if idx == len(ones):
                ans = flips
                return
            r = ones[idx][0]
            c = ones[idx][1]
            changed = []
            for j in range(n):
                if grid[r][j] == 1:
                    grid[r][j] = 0
                    changed.append([r, j])
            dfs(idx + 1, flips + 1)
            for x, y in changed:
                grid[x][y] = 1
            changed = []
            for i in range(m):
                if grid[i][c] == 1:
                    grid[i][c] = 0
                    changed.append([i, c])
            dfs(idx + 1, flips + 1)
            for x, y in changed:
                grid[x][y] = 1

        dfs(0, 0)
        return ans
