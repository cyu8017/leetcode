# LeetCode 0329 - Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        @lru_cache(maxsize=None)
        def dfs(row: int, col: int) -> int:
            best = 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[row][col]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        return max(dfs(row, col) for row in range(rows) for col in range(cols))
