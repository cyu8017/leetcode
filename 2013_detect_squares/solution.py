# LeetCode 2013 - Detect Squares
# https://leetcode.com/problems/detect-squares/

from typing import List


class DetectSquares:
    def __init__(self):
        self.cnt = {}

    def _key(self, x: int, y: int) -> str:
        return f"{x},{y}"

    def add(self, point: List[int]) -> None:
        k = self._key(point[0], point[1])
        self.cnt[k] = self.cnt.get(k, 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        ans = 0
        for k, c in self.cnt.items():
            px, py = map(int, k.split(","))
            if px == x or py == y:
                continue
            if abs(px - x) != abs(py - y):
                continue
            c1 = self.cnt.get(self._key(px, y), 0)
            c2 = self.cnt.get(self._key(x, py), 0)
            ans += c * c1 * c2
        return ans
