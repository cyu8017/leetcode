# LeetCode 0631 - Design Excel Sum Formula
# https://leetcode.com/problems/design-excel-sum-formula/

from typing import List


class Excel:
    def __init__(self, height: int, width: str):
        self.height = height
        self.width = ord(width) - ord("A") + 1
        self.values = [[0] * self.width for _ in range(height + 1)]
        self.formulas: dict[tuple[int, int], list[tuple[int, int]]] = {}

    def set(self, row: int, column: str, val: int) -> None:
        col = ord(column) - ord("A")
        self.formulas.pop((row, col), None)
        self.values[row][col] = val

    def get(self, row: int, column: str) -> int:
        return self._eval(row, ord(column) - ord("A"))

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        col = ord(column) - ord("A")
        cells: list[tuple[int, int]] = []
        for token in numbers:
            if ":" in token:
                start, end = token.split(":")
                r1, c1 = self._parse(start)
                r2, c2 = self._parse(end)
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        cells.append((r, c))
            else:
                cells.append(self._parse(token))
        self.formulas[(row, col)] = cells
        return self._eval(row, col)

    def _parse(self, cell: str) -> tuple[int, int]:
        return int(cell[1:]), ord(cell[0]) - ord("A")

    def _eval(self, row: int, col: int) -> int:
        if (row, col) in self.formulas:
            return sum(self._eval(r, c) for r, c in self.formulas[(row, col)])
        return self.values[row][col]
