# LeetCode 3565 - Sequential Grid Path Cover
# https://leetcode.com/problems/sequential-grid-path-cover/

from typing import List


class Solution:
    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dirs = [-1, 0, 1, 0, -1]
        st = 0
        path = []

        def f(i: int, j: int) -> int:
            return i * n + j

        def dfs(i: int, j: int, v: int) -> bool:
            nonlocal st
            path.append([i, j])
            if len(path) == m * n:
                return True
            idx = f(i, j)
            st |= 1 << idx
            if grid[i][j] == v:
                v += 1
            for t in range(4):
                x, y = i + dirs[t], j + dirs[t + 1]
                if 0 <= x < m and 0 <= y < n:
                    idx2 = f(x, y)
                    if ((st >> idx2) & 1) == 0 and (grid[x][y] == 0 or grid[x][y] == v):
                        if dfs(x, y, v):
                            return True
            path.pop()
            st ^= 1 << idx
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    if dfs(i, j, 1):
                        return path
                    path.clear()
                    st = 0
        return []
