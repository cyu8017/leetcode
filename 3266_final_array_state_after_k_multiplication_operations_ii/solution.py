# LeetCode 3266 - Final Array State After K Multiplication Operations II
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

from typing import Any, Callable, List, Optional


class MinHeap:
    def __init__(self, cmp: Optional[Callable] = None):
        self.a: List[Any] = []
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
        a, cmp, n = self.a, self.cmp, len(self.a)
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

    def push(self, x: Any) -> None:
        self.a.append(x)
        self._up(len(self.a) - 1)

    def pop(self) -> Any:
        a = self.a
        if not a:
            return None
        top = a[0]
        last = a.pop()
        if a:
            a[0] = last
            self._down(0)
        return top

    def peek(self) -> Any:
        return self.a[0]

    def size(self) -> int:
        return len(self.a)



class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        mod = 1000000007

        def modPow(a: int, e: int, mod: int) -> int:
            r = 1
            a %= mod
            while e > 0:
                if e & 1:
                    r = (r * a) % mod
                a = (a * a) % mod
                e >>= 1
            return r

        if multiplier == 1:
            return nums
        h = MinHeap(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1])
        maxV = 0
        for i in range(len(nums)):
            h.push([nums[i], i])
            if nums[i] > maxV:
                maxV = nums[i]
        while k > 0 and h.size():
            cur = h.pop()
            v, i = cur[0], cur[1]
            if v * multiplier > maxV and k >= len(nums):
                h.push([v, i])
                break
            nv = v * multiplier
            nums[i] = nv
            if nv > maxV:
                maxV = nv
            h.push([nv, i])
            k -= 1
        if k > 0:
            n = len(nums)
            full, rem = k // n, k % n
            powFull = modPow(multiplier, full, mod)
            for i in range(n):
                nums[i] = (nums[i] * powFull) % mod
            hh = MinHeap(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1])
            for i in range(n):
                hh.push([nums[i], i])
            for t in range(rem):
                cur = hh.pop()
                v = (cur[0] * multiplier) % mod
                i = cur[1]
                nums[i] = v
                hh.push([v, i])
            for i in range(n):
                nums[i] %= mod
        else:
            for i in range(len(nums)):
                nums[i] %= mod
        return nums
