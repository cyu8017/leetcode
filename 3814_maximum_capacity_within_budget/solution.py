# LeetCode 3814 - Maximum Capacity Within Budget
# https://leetcode.com/problems/maximum-capacity-within-budget/

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
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        arr = []
        for k in range(len(costs)):
            if costs[k] < budget:
                arr.append([costs[k], capacity[k]])
        if not arr:
            return 0
        arr.sort(key=lambda x: x[0])
        m = len(arr)
        alive = [True] * m
        h = MinHeap(lambda a, b: (b[0] - a[0]) if a[0] != b[0] else (b[1] - a[1]))
        for i in range(m):
            h.push([arr[i][1], i])
        while h.size() and not alive[h.peek()[1]]:
            h.pop()
        ans = h.peek()[0]
        i, j = 0, m - 1
        while i < j:
            alive[i] = False
            while i < j and arr[i][0] + arr[j][0] >= budget:
                alive[j] = False
                j -= 1
            while h.size() and not alive[h.peek()[1]]:
                h.pop()
            if h.size():
                ans = max(ans, arr[i][1] + h.peek()[0])
            i += 1
        return ans
