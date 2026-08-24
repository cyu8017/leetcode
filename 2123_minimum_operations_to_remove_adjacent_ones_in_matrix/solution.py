# LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
# https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

from typing import List
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        id = [[-1] * (n) for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    id[i][j] = cnt
                    cnt += 1
        g = [[] for _ in range(cnt)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1 or (i + j) % 2 != 0:
                    continue
                u = id[i][j]
                for di, dj in dirs:
                    ni = i + di
                    nj = j + dj
                    if ni >= 0 and nj >= 0 and ni < m and nj < n and grid[ni][nj] == 1:
                        g[u].append(id[ni][nj])
        match = [-1] * (cnt)
        def dfs(u, seen):
            for v in g[u]:
                if seen[v]:
                    continue
                seen[v] = True
                if match[v] == -1 or dfs(match[v], seen):
                    match[v] = u
                    return True
            return False

        ans = 0
        for u in range(cnt):
            ok = False
            i = 0
            while i < m and not ok:
                for j in range(n):
                    if id[i][j] == u and (i + j) % 2 == 0:
                        ok = True
                        break
                i += 1
            if not ok:
                continue
            seen = [False] * (cnt)
            if dfs(u, seen):
                ans += 1
        return ans
