# LeetCode 2187 - Minimum Time to Complete Trips
# https://leetcode.com/problems/minimum-time-to-complete-trips/

from typing import List
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        mn = time[0]
        for t in time:
            mn = min(mn, t)
        lo = 1
        hi = mn * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            trips = 0
            ok = False
            for t in time:
                trips += mid // t
                if trips >= totalTrips:
                    ok = True
                    break
            if ok:
                hi = mid
            else:
                lo = mid + 1
        return lo
