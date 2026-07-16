# LeetCode 1066 - Campus Bikes II
# https://leetcode.com/problems/campus-bikes-ii/

from functools import lru_cache


class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        m = len(bikes)

        @lru_cache(None)
        def dp(i: int, mask: int) -> int:
            if i == len(workers):
                return 0
            best = float("inf")
            wx, wy = workers[i]
            for b in range(m):
                if mask & (1 << b):
                    continue
                bx, by = bikes[b]
                dist = abs(wx - bx) + abs(wy - by)
                best = min(best, dist + dp(i + 1, mask | (1 << b)))
            return best

        return int(dp(0, 0))
