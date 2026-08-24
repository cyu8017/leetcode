# LeetCode 3538 - Merge Operations for Minimum Travel Time
# https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

from typing import List


class Solution:
    def minTravelTime(
        self, l: int, n: int, k: int, position: List[int], time: List[int]
    ) -> int:
        prefix = [0] * n
        prefix[0] = time[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + time[i]
        memo = {}
        INF = 10**18

        def dp(i: int, skips: int, last: int) -> int:
            if i == n - 1:
                return 0 if skips == 0 else INF
            key = (i, skips, last)
            if key in memo:
                return memo[key]
            rate = prefix[i]
            if last > 0:
                rate -= prefix[last - 1]
            res = INF
            end = n - 1
            if i + skips + 1 < end:
                end = i + skips + 1
            for j in range(i + 1, end + 1):
                cand = (position[j] - position[i]) * rate + dp(j, skips - (j - i - 1), i + 1)
                if cand < res:
                    res = cand
            memo[key] = res
            return res

        return dp(0, k, 0)
