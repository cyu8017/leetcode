# LeetCode 3733 - Minimum Time to Complete All Deliveries
# https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

from typing import List


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        def ok(T: int) -> bool:
            w0 = T - T // r[0]
            w1 = T - T // r[1]
            return w0 + w1 >= d[0] + d[1]

        lo, hi = 1, 10**18
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
