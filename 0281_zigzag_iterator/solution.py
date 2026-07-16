# LeetCode 0281 - Zigzag Iterator
# https://leetcode.com/problems/zigzag-iterator/

from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.indices = [0, 0]
        self.turn = 0

    def next(self) -> int:
        while self.indices[self.turn] >= len(self.vectors[self.turn]):
            self.turn = 1 - self.turn
        value = self.vectors[self.turn][self.indices[self.turn]]
        self.indices[self.turn] += 1
        self.turn = 1 - self.turn
        return value

    def hasNext(self) -> bool:
        return any(
            self.indices[index] < len(self.vectors[index])
            for index in range(len(self.vectors))
        )
