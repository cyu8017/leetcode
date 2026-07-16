# LeetCode 0317 - Shortest Distance from All Buildings
# https://leetcode.com/problems/shortest-distance-from-all-buildings/

from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        buildings = sum(cell == 1 for row in grid for cell in row)
        distances = [[0] * cols for _ in range(rows)]
        reach = [[0] * cols for _ in range(rows)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                queue: deque[tuple[int, int, int]] = deque([(row, col, 0)])
                visited = {(row, col)}
                while queue:
                    current_row, current_col, distance = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = current_row + dr, current_col + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 0
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            distances[nr][nc] += distance + 1
                            reach[nr][nc] += 1
                            queue.append((nr, nc, distance + 1))

        best = float("inf")
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and reach[row][col] == buildings:
                    best = min(best, distances[row][col])
        return -1 if best == float("inf") else best
