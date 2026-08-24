# LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
# https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

from typing import List


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        pn = [0] * (n + 1)
        pc = [0] * (n + 1)
        for i in range(n):
            pn[i + 1] = pn[i] + nums[i]
            pc[i + 1] = pc[i] + cost[i]
        inf = 10**18
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i] = inf
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1]
                if cand < dp[i]:
                    dp[i] = cand
        return dp[0]
