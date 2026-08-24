# LeetCode 2036 - Maximum Alternating Subarray Sum
# https://leetcode.com/problems/maximum-alternating-subarray-sum/

from typing import List


class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        ans = -10**18
        even = 0
        for i, x in enumerate(nums):
            if i % 2 == 0:
                even += x
            else:
                even = max(0, even - x)
            ans = max(ans, even)
        odd = 0
        for i in range(1, len(nums)):
            x = nums[i]
            if i % 2 == 1:
                odd += x
            else:
                odd = max(0, odd - x)
            ans = max(ans, odd)
        return ans
