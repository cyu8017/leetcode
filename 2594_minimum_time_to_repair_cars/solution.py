# LeetCode 2594 - Minimum Time to Repair Cars
# https://leetcode.com/problems/minimum-time-to-repair-cars/

from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mn = min(ranks)
        lo, hi = 1, mn * cars * cars

        def ok(t: int) -> bool:
            done = 0
            for r in ranks:
                l, h = 0, cars
                while l < h:
                    mid = (l + h + 1) // 2
                    if r * mid * mid <= t:
                        l = mid
                    else:
                        h = mid - 1
                done += l
                if done >= cars:
                    return True
            return done >= cars

        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
