# LeetCode 0407 - Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/

import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows = len(heightMap)
        cols = len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0

        visited = [[False] * cols for _ in range(rows)]
        heap: list[tuple[int, int, int]] = []

        for row in range(rows):
            for col in range(cols):
                if row in (0, rows - 1) or col in (0, cols - 1):
                    heapq.heappush(heap, (heightMap[row][col], row, col))
                    visited[row][col] = True

        trapped = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while heap:
            height, row, col = heapq.heappop(heap)
            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc
                if not (0 <= next_row < rows and 0 <= next_col < cols) or visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                next_height = heightMap[next_row][next_col]
                trapped += max(0, height - next_height)
                heapq.heappush(heap, (max(height, next_height), next_row, next_col))

        return trapped
