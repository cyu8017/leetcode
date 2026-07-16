# LeetCode 0542 - 01 Matrix
# https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[10**9] * cols for _ in range(rows)]
        queue: deque[tuple[int, int]] = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                    queue.append((row, col))

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[row][col] + 1:
                    dist[nr][nc] = dist[row][col] + 1
                    queue.append((nr, nc))

        return dist
