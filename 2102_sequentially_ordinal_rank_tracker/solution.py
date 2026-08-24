# LeetCode 2102 - Sequentially Ordinal Rank Tracker
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

import heapq


class _Rev:
    def __init__(self, s: str):
        self.s = s

    def __lt__(self, other: "_Rev") -> bool:
        return self.s > other.s


class SORTracker:
    def __init__(self):
        self.best = []
        self.rest = []
        self.k = 0

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.best, (score, _Rev(name), name))
        if len(self.best) > self.k:
            sc, _, nm = heapq.heappop(self.best)
            heapq.heappush(self.rest, (-sc, nm))

    def get(self) -> str:
        self.k += 1
        if self.rest:
            sc, nm = heapq.heappop(self.rest)
            heapq.heappush(self.best, (-sc, _Rev(nm), nm))
        return self.best[0][2]
