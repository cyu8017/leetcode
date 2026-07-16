# LeetCode 0494 - Target Sum
# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 or abs(target) > total:
            return 0
        need = (total + target) // 2
        dp = [0] * (need + 1)
        dp[0] = 1
        for num in nums:
            for amount in range(need, num - 1, -1):
                dp[amount] += dp[amount - num]
        return dp[need]
