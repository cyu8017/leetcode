# LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for it in intervals:
            events.append((it[0], 1))
            events.append((it[1] + 1, -1))
        events.sort(key=lambda e: (e[0], e[1]))
        cur = ans = 0
        for _, d in events:
            cur += d
            ans = max(ans, cur)
        return ans
