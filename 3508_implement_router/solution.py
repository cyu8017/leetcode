# LeetCode 3508 - Implement Router
# https://leetcode.com/problems/implement-router/

from typing import List


def lowerBound(a: List[int], frm: int, target: int) -> int:
    lo, hi = frm, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Router:
    def __init__(self, memoryLimit: int):
        self.lim = memoryLimit
        self.vis = set()
        self.q = []
        self.idx = {}
        self.d = {}

    def f(self, a: int, b: int, c: int) -> int:
        return (a << 46) | (b << 29) | c

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        x = self.f(source, destination, timestamp)
        if x in self.vis:
            return False
        self.vis.add(x)
        if len(self.q) >= self.lim:
            self.forwardPacket()
        self.q.append([source, destination, timestamp])
        if destination not in self.d:
            self.d[destination] = []
        self.d[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        packet = self.q.pop(0)
        s, dest, t = packet[0], packet[1], packet[2]
        self.vis.discard(self.f(s, dest, t))
        self.idx[dest] = self.idx.get(dest, 0) + 1
        return [s, dest, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ls = self.d.get(destination)
        if not ls:
            return 0
        k = self.idx.get(destination, 0)
        return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime)
