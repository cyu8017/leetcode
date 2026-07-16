# LeetCode 0251 - Flatten 2D Vector
# https://leetcode.com/problems/flatten-2d-vector/

from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0
        self._advance()

    def _advance(self) -> None:
        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0

    def next(self) -> int:
        value = self.vec[self.row][self.col]
        self.col += 1
        self._advance()
        return value

    def hasNext(self) -> bool:
        self._advance()
        return self.row < len(self.vec)
