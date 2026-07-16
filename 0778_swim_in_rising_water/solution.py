# LeetCode 0778 - Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        while heap:
            time, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return time
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
        return -1
