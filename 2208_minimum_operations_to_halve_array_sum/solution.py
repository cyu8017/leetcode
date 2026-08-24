# LeetCode 2208 - Minimum Operations to Halve Array Sum
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

from typing import List
class MinHeap:
    def __init__(self, cmp):
        self.a = []
        self.cmp = cmp or (lambda x, y: x - y)

    def _up(self, i):
        a = self.a
        cmp = self.cmp
        while i > 0:
            p = (i - 1) >> 1
            if cmp(a[i], a[p]) >= 0:
                break
            a[i], a[p] = a[p], a[i]
            i = p

    def _down(self, i):
        a = self.a
        cmp = self.cmp
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

    def push(self, x):
        self.a.append(x)
        self._up(len(self.a) - 1)

    def pop(self):
        a = self.a
        if not len(a):
            return None
        top = a[0]
        last = a.pop()
        if a:
            a[0] = last
            self._down(0)
        return top

    def size(self):
        return len(self.a)

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        h = MinHeap(lambda a, b: b - a)
        sum = 0
        for x in nums:
            h.push(x)
            sum += x
        target = sum / 2
        ans = 0
        while sum > target:
            top = h.pop()
            x = top / 2
            sum -= x
            h.push(x)
            ans += 1
        return ans
