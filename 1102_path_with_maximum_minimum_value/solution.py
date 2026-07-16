# LeetCode 1102 - Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/

import heapq


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(-grid[0][0], 0, 0)]
        seen = {(0, 0)}
        while heap:
            val, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return -val
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(heap, (max(val, -grid[nr][nc]), nr, nc))
        return grid[0][0]
