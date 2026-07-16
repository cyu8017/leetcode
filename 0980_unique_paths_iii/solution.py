# LeetCode 0980 - Unique Paths III
# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        empty = 0
        sr = sc = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    empty += 1
                if grid[i][j] == 1:
                    sr, sc = i, j
        self.ans = 0

        def dfs(r: int, c: int, remain: int) -> None:
            if grid[r][c] == 2:
                if remain == 1:
                    self.ans += 1
                return
            temp = grid[r][c]
            grid[r][c] = -1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    dfs(nr, nc, remain - 1)
            grid[r][c] = temp

        dfs(sr, sc, empty)
        return self.ans
