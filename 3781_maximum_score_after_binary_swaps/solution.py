# LeetCode 3781 - Maximum Score After Binary Swaps
# https://leetcode.com/problems/maximum-score-after-binary-swaps/

from typing import Callable, List, Optional


class MinHeap:
    def __init__(self, cmp: Optional[Callable] = None):
        self.a = []
        self.cmp = cmp or (lambda x, y: x - y)

    def _up(self, i: int) -> None:
        a, cmp = self.a, self.cmp
        while i > 0:
            p = (i - 1) >> 1
            if cmp(a[i], a[p]) >= 0:
                break
            a[i], a[p] = a[p], a[i]
            i = p

    def _down(self, i: int) -> None:
        a, cmp = self.a, self.cmp
        n = len(a)
        while True:
            s = i
            l = i * 2 + 1
            r = l + 1
            if l < n and cmp(a[l], a[s]) < 0:
                s = l
            if r < n and cmp(a[r], a[s]) < 0:
                s = r
            if s == i:
                break
            a[i], a[s] = a[s], a[i]
            i = s

    def push(self, x) -> None:
        self.a.append(x)
        self._up(len(self.a) - 1)

    def pop(self):
        a = self.a
        if not a:
            return None
        top = a[0]
        last = a.pop()
        if a:
            a[0] = last
            self._down(0)
        return top

    def peek(self):
        return self.a[0]

    def size(self) -> int:
        return len(self.a)


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        ans = 0
        pq = MinHeap(lambda a, b: b - a)
        for i, x in enumerate(nums):
            pq.push(x)
            if s[i] == "1":
                ans += pq.pop()
        return ans
