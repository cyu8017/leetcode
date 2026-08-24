# LeetCode 3102 - Minimize Manhattan Distances
# https://leetcode.com/problems/minimize-manhattan-distances/

import bisect
from typing import List


class _MultiSet:
    def __init__(self):
        self.m = {}
        self.keys = []

    def merge(self, x: int, v: int) -> None:
        nv = self.m.get(x, 0) + v
        if nv == 0:
            del self.m[x]
            i = bisect.bisect_left(self.keys, x)
            if i < len(self.keys) and self.keys[i] == x:
                self.keys.pop(i)
        else:
            if x not in self.m:
                bisect.insort(self.keys, x)
            self.m[x] = nv

    def first(self) -> int:
        return self.keys[0]

    def last(self) -> int:
        return self.keys[-1]


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        st1 = _MultiSet()
        st2 = _MultiSet()
        for p in points:
            st1.merge(p[0] + p[1], 1)
            st2.merge(p[0] - p[1], 1)
        ans = 10**18
        for p in points:
            x, y = p[0], p[1]
            st1.merge(x + y, -1)
            st2.merge(x - y, -1)
            ans = min(ans, max(st1.last() - st1.first(), st2.last() - st2.first()))
            st1.merge(x + y, 1)
            st2.merge(x - y, 1)
        return ans
