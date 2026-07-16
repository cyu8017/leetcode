# LeetCode 0304 - Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                self.prefix[row + 1][col + 1] = (
                    matrix[row][col]
                    + self.prefix[row][col + 1]
                    + self.prefix[row + 1][col]
                    - self.prefix[row][col]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_left = self.prefix[row1][col1]
        top_right = self.prefix[row1][col2 + 1]
        bottom_left = self.prefix[row2 + 1][col1]
        bottom_right = self.prefix[row2 + 1][col2 + 1]
        return bottom_right - top_right - bottom_left + top_left
