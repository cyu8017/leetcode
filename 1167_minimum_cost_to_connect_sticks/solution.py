# LeetCode 1167 - Minimum Cost to Connect Sticks
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/

import heapq


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        if len(sticks) <= 1:
            return 0
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            ans += cost
            heapq.heappush(sticks, cost)
        return ans
