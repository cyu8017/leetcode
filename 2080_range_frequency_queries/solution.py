# LeetCode 2080 - Range Frequency Queries
# https://leetcode.com/problems/range-frequency-queries/

from typing import List


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.pos = {}
        for i, v in enumerate(arr):
            self.pos.setdefault(v, []).append(i)

    def lower(self, p: List[int], x: int) -> int:
        lo, hi = 0, len(p)
        while lo < hi:
            mid = (lo + hi) >> 1
            if p[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper(self, p: List[int], x: int) -> int:
        lo, hi = 0, len(p)
        while lo < hi:
            mid = (lo + hi) >> 1
            if p[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def query(self, left: int, right: int, value: int) -> int:
        p = self.pos.get(value)
        if not p:
            return 0
        return self.upper(p, right) - self.lower(p, left)
