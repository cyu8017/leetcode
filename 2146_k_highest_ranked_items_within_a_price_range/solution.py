# LeetCode 2146 - K Highest Ranked Items Within a Price Range
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

from typing import List
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        low = pricing[0]
        high = pricing[1]
        vis = [[False] * (n) for _ in range(m)]
        q = [[start[0], start[1], 0]]
        vis[start[0]][start[1]] = True
        cands = []
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c, d = q.pop(0)
            if grid[r][c] >= low and grid[r][c] <= high:
                cands.append([d, grid[r][c], r, c])
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < m and nc >= 0 and nc < n and not vis[nr][nc] and grid[nr][nc] != 0:
                    vis[nr][nc] = True
                    q.append([nr, nc, d + 1])
        cands.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
        if k > len(cands):
            k = len(cands)
        ans = []
        for i in range(k):
            ans.append([cands[i][2], cands[i][3]])
        return ans
