# LeetCode 2297 - Jump Game VIII
# https://leetcode.com/problems/jump-game-viii/

from typing import List


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        stack1, stack2 = [], []
        for i in range(n):
            while stack1 and nums[stack1[-1]] <= nums[i]:
                j = stack1.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])
            while stack2 and nums[stack2[-1]] > nums[i]:
                j = stack2.pop()
                dp[i] = min(dp[i], dp[j] + costs[i])
            if stack1:
                dp[i] = min(dp[i], dp[stack1[-1]] + costs[i])
            if stack2:
                dp[i] = min(dp[i], dp[stack2[-1]] + costs[i])
            stack1.append(i)
            stack2.append(i)
        return int(dp[n - 1])
