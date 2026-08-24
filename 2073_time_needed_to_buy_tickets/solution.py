# LeetCode 2073 - Time Needed to Buy Tickets
# https://leetcode.com/problems/time-needed-to-buy-tickets/

from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i, t in enumerate(tickets):
            if i <= k:
                ans += min(t, tickets[k])
            else:
                ans += min(t, tickets[k] - 1)
        return ans
