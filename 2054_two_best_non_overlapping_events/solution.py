# LeetCode 2054 - Two Best Non-Overlapping Events
# https://leetcode.com/problems/two-best-non-overlapping-events/

from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[0])
        n = len(events)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i + 1], events[i][2])
        ans = 0
        for i in range(n):
            ans = max(ans, events[i][2])
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) >> 1
                if events[mid][0] > events[i][1]:
                    hi = mid
                else:
                    lo = mid + 1
            if lo < n:
                ans = max(ans, events[i][2] + suffix[lo])
        return ans
