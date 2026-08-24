# LeetCode 3979 - Maximum Valid Pair Sum
# https://leetcode.com/problems/maximum-valid-pair-sum/

from typing import List


class Solution:
    def maxValidPairSum(self, nums: List[int], k: int) -> int:
        ans = 0
        x = 0
        for j in range(k, len(nums)):
            y = nums[j]
            x = max(x, nums[j - k])
            ans = max(ans, x + y)
        return ans
