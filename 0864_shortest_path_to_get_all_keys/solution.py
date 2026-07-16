# LeetCode 0864 - Shortest Path to Get All Keys
# https://leetcode.com/problems/shortest-path-to-get-all-keys/

from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        all_keys = 0
        start = (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i, j)
                elif "a" <= grid[i][j] <= "f":
                    all_keys |= 1 << (ord(grid[i][j]) - 97)
        queue = deque([(start[0], start[1], 0, 0)])
        seen = {(start[0], start[1], 0)}
        while queue:
            r, c, mask, dist = queue.popleft()
            if mask == all_keys:
                return dist
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] == "#":
                    continue
                cell = grid[nr][nc]
                nmask = mask
                if "a" <= cell <= "f":
                    nmask |= 1 << (ord(cell) - 97)
                if "A" <= cell <= "F" and not (mask & (1 << (ord(cell) - 65))):
                    continue
                state = (nr, nc, nmask)
                if state not in seen:
                    seen.add(state)
                    queue.append((nr, nc, nmask, dist + 1))
        return -1
