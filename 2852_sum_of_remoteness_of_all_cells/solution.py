# LeetCode 2852 - Sum of Remoteness of All Cells
# https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

from typing import List


class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total += grid[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1 or seen[i][j]:
                    continue
                q = [(i, j)]
                seen[i][j] = True
                sm = 0
                cnt = 0
                h = 0
                while h < len(q):
                    x, y = q[h]
                    h += 1
                    sm += grid[x][y]
                    cnt += 1
                    for dx, dy in dirs:
                        ni, nj = x + dx, y + dy
                        if 0 <= ni < m and 0 <= nj < n and not seen[ni][nj] and grid[ni][nj] != -1:
                            seen[ni][nj] = True
                            q.append((ni, nj))
                ans += (total - sm) * cnt
        return ans
