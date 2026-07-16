# LeetCode 0774 - Minimize Max Distance to Gas Station
# https://leetcode.com/problems/minimize-max-distance-to-gas-station/

from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def can(dist: float) -> bool:
            needed = 0
            for i in range(1, len(stations)):
                needed += int((stations[i] - stations[i - 1]) / dist)
            return needed <= k

        lo, hi = 0.0, float(stations[-1] - stations[0])
        while hi - lo > 1e-6:
            mid = (lo + hi) / 2
            if can(mid):
                hi = mid
            else:
                lo = mid
        return hi
