# LeetCode 2369 - Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if i >= 2 and nums[i - 1] == nums[i - 2] and dp[i - 2]:
                dp[i] = True
            if i >= 3 and nums[i - 1] == nums[i - 2] == nums[i - 3] and dp[i - 3]:
                dp[i] = True
            if i >= 3 and nums[i - 1] == nums[i - 2] + 1 and nums[i - 2] == nums[i - 3] + 1 and dp[i - 3]:
                dp[i] = True
        return dp[n]
