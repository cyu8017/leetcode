# LeetCode 2812 - Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        h = 0
        while h < len(q):
            x, y = q[h]
            h += 1
            for dx, dy in dirs:
                ni, nj = x + dx, y + dy
                if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[x][y] + 1
                    q.append((ni, nj))

        def ok(sf: int) -> bool:
            if dist[0][0] < sf:
                return False
            seen = [[False] * n for _ in range(n)]
            st = [(0, 0)]
            seen[0][0] = True
            while st:
                x, y = st.pop()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in dirs:
                    ni, nj = x + dx, y + dy
                    if 0 <= ni < n and 0 <= nj < n and not seen[ni][nj] and dist[ni][nj] >= sf:
                        seen[ni][nj] = True
                        st.append((ni, nj))
            return False

        lo, hi, ans = 0, n * n, 0
        while lo <= hi:
            mid = (lo + hi) >> 1
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
