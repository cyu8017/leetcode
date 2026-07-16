# LeetCode 0286 - Walls and Gates
# https://leetcode.com/problems/walls-and-gates/

from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        rows, cols = len(rooms), len(rooms[0])
        queue: deque[tuple[int, int]] = deque()
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))
        while queue:
            row, col = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[row][col] + 1
                    queue.append((nr, nc))
