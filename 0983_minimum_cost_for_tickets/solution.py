# LeetCode 0983 - Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dayset = set(days)
        last = days[-1]
        dp = [0] * (last + 1)
        for d in range(1, last + 1):
            if d not in dayset:
                dp[d] = dp[d - 1]
            else:
                dp[d] = min(
                    dp[d - 1] + costs[0],
                    dp[max(0, d - 7)] + costs[1],
                    dp[max(0, d - 30)] + costs[2],
                )
        return dp[last]
