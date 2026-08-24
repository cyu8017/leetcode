# LeetCode 3049 - Earliest Second to Mark Indices II
# https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

from typing import Callable, List, Optional


class MinHeap:
    def __init__(self, cmp: Optional[Callable] = None):
        self.a = []
        self.cmp = cmp or (lambda x, y: x - y)

    def _up(self, i: int) -> None:
        a = self.a
        cmp = self.cmp
        while i > 0:
            p = (i - 1) >> 1
            if cmp(a[i], a[p]) >= 0:
                break
            a[i], a[p] = a[p], a[i]
            i = p

    def _down(self, i: int) -> None:
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
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def getSecondToIndex(nums, changeIndices):
            indexToFirstSecond = {}
            for second in range(len(changeIndices)):
                index = changeIndices[second] - 1
                if nums[index] > 0 and index not in indexToFirstSecond:
                    indexToFirstSecond[index] = second
            secondToIndex = {}
            for idx, sec in indexToFirstSecond.items():
                secondToIndex[sec] = idx
            return secondToIndex

        def canMark(nums, secondToIndex, maxSecond, numsSum):
            h = MinHeap()
            marks = 0
            for second in range(maxSecond - 1, -1, -1):
                if second in secondToIndex:
                    h.push(nums[secondToIndex[second]])
                    if marks == 0:
                        h.pop()
                        marks += 1
                    else:
                        marks -= 1
                else:
                    marks += 1
            heapSize = h.size()
            heapSum = 0
            while h.size():
                heapSum += h.pop()
            decrementAndMarkCost = numsSum - heapSum + (len(nums) - heapSize)
            zeroAndMarkCost = heapSize + heapSize
            return decrementAndMarkCost + zeroAndMarkCost <= maxSecond

        secondToIndex = getSecondToIndex(nums, changeIndices)
        numsSum = 0
        for v in nums:
            numsSum += v
        l = 0
        r = len(changeIndices) + 1
        while l < r:
            m = (l + r) // 2
            if canMark(nums, secondToIndex, m, numsSum):
                r = m
            else:
                l = m + 1
        return l if l <= len(changeIndices) else -1
