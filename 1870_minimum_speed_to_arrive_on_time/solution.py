# LeetCode 1870 - Minimum Speed to Arrive on Time
# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if n - 1 >= hour:
            return -1

        def can_arrive(speed: int) -> bool:
            time = 0.0
            for i in range(n - 1):
                time += (dist[i] + speed - 1) // speed
            time += dist[-1] / speed
            return time <= hour

        if not can_arrive(10**7):
            return -1

        lo, hi = 1, 10**7
        while lo < hi:
            mid = (lo + hi) // 2
            if can_arrive(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
