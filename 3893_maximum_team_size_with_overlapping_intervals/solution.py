# LeetCode 3893 - Maximum Team Size With Overlapping Intervals
# https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

from typing import List


class Solution:
    def maximumTeamSize(self, startTime: List[int], endTime: List[int]) -> int:
        def upper_bound(a: List[int], x: int) -> int:
            lo = 0
            hi = len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        n = len(startTime)
        st = sorted(startTime)
        en = sorted(endTime)
        ans = 0
        for t in range(n):
            l = startTime[t]
            r = endTime[t]
            i = upper_bound(en, l - 1)
            j = upper_bound(st, r)
            ans = max(ans, j - i)
        return ans
