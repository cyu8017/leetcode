# LeetCode 4009 - Minimum Possible Maximum Waiting Time
# https://leetcode.com/problems/minimum-possible-maximum-waiting-time/

from typing import List


class Solution:
    def packKey(self, i: int, f0: int, f1: int, d0: int, d1: int) -> int:
        return ((((i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1)

    def maxServe(self, i: int, f0: int, f1: int, d0: int, d1: int) -> int:
        if i == self.n:
            return i
        key = self.packKey(i, f0, f1, d0, d1)
        if key in self.memo:
            return self.memo[key]
        need = self.dem[i]
        can0 = f0 >= need
        can1 = f1 >= need
        best = i
        if not can0 and not can1:
            self.memo[key] = best
            return best
        if can0:
            nd1 = d1 - d0 if d1 > d0 else 0
            best = max(best, self.maxServe(i + 1, f0 - need, f1, need, nd1))
        if can1:
            nd0 = d0 - d1 if d0 > d1 else 0
            best = max(best, self.maxServe(i + 1, f0, f1 - need, nd0, need))
        self.memo[key] = best
        return best

    def canWithW(self, i: int, f0: int, f1: int, d0: int, d1: int) -> bool:
        if i >= self.bestServe:
            return True
        if i == self.n:
            return True
        key = self.packKey(i, f0, f1, d0, d1)
        if key in self.memo:
            return self.memo[key] == 2
        need = self.dem[i]
        can0 = f0 >= need
        can1 = f1 >= need
        ok = False
        if not can0 and not can1:
            self.memo[key] = 1
            return False
        if can0 and d0 <= self.W:
            nd1 = d1 - d0 if d1 > d0 else 0
            if self.canWithW(i + 1, f0 - need, f1, need, nd1):
                ok = True
        if not ok and can1 and d1 <= self.W:
            nd0 = d0 - d1 if d0 > d1 else 0
            if self.canWithW(i + 1, f0, f1 - need, nd0, need):
                ok = True
        self.memo[key] = 2 if ok else 1
        return ok

    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        self.dem = demand
        self.n = len(demand)
        f0, f1 = fuel[0], fuel[1]
        if f0 < demand[0] and f1 < demand[0]:
            return -1
        self.memo = {}
        self.bestServe = self.maxServe(0, f0, f1, 0, 0)
        if self.bestServe == 0:
            return -1
        lo = 0
        hi = 0
        for x in demand:
            hi += x
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            self.W = mid
            self.memo = {}
            if self.canWithW(0, f0, f1, 0, 0):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
