# LeetCode 3619 - Count Islands With Total Value Divisible by K
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

from typing import List


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]

        def dfs(i: int, j: int) -> int:
            s = grid[i][j]
            grid[i][j] = 0
            for d in range(4):
                x, y = i + dirs[d], j + dirs[d + 1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    s += dfs(x, y)
            return s

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and dfs(i, j) % k == 0:
                    ans += 1
        return ans
