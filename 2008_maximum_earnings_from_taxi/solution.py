# LeetCode 2008 - Maximum Earnings From Taxi
# https://leetcode.com/problems/maximum-earnings-from-taxi/

from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda r: r[1])
        m = len(rides)
        ends = [r[1] for r in rides]
        dp = [0] * (m + 1)
        for i, (start, end, tip) in enumerate(rides):
            earn = end - start + tip
            lo, hi = 0, m
            while lo < hi:
                mid = (lo + hi) >> 1
                if ends[mid] <= start:
                    lo = mid + 1
                else:
                    hi = mid
            dp[i + 1] = max(dp[i], earn + dp[lo])
        return dp[m]
