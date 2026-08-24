# LeetCode 2270 - Number of Ways to Split Array
# https://leetcode.com/problems/number-of-ways-to-split-array/

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left = ans = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= total - left:
                ans += 1
        return ans
