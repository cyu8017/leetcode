# LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

from typing import Callable, Optional


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
    def minimizeStringValue(self, s: str) -> str:
        cnt = [0] * 26
        k = 0
        for c in s:
            if c == "?":
                k += 1
            else:
                cnt[ord(c) - 97] += 1
        pq = MinHeap(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1])
        for i in range(26):
            pq.push([cnt[i], i])
        t = [0] * k
        for i in range(k):
            p = pq.pop()
            t[i] = p[1]
            p[0] += 1
            pq.push(p)
        t.sort()
        arr = list(s)
        j = 0
        for i in range(len(arr)):
            if arr[i] == "?":
                arr[i] = chr(t[j] + 97)
                j += 1
        return "".join(arr)
