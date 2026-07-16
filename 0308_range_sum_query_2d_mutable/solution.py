# LeetCode 0308 - Range Sum Query 2D - Mutable
# https://leetcode.com/problems/range-sum-query-2d-mutable/

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows else 0
        self.tree = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        def add(row: int, col: int, delta: int) -> None:
            row_index = row
            while row_index <= self.rows:
                col_index = col
                while col_index <= self.cols:
                    self.tree[row_index][col_index] += delta
                    col_index += col_index & -col_index
                row_index += row_index & -row_index

        for row in range(self.rows):
            for col in range(self.cols):
                add(row + 1, col + 1, matrix[row][col])

        self._add = add

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._add(row + 1, col + 1, delta)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def prefix(row: int, col: int) -> int:
            total = 0
            row_index = row
            while row_index > 0:
                col_index = col
                while col_index > 0:
                    total += self.tree[row_index][col_index]
                    col_index -= col_index & -col_index
                row_index -= row_index & -row_index
            return total

        return (
            prefix(row2 + 1, col2 + 1)
            - prefix(row1, col2 + 1)
            - prefix(row2 + 1, col1)
            + prefix(row1, col1)
        )
