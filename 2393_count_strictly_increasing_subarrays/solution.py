# LeetCode 2393 - Count Strictly Increasing Subarrays
# https://leetcode.com/problems/count-strictly-increasing-subarrays/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = length = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] > nums[i - 1]:
                length += 1
            else:
                length = 1
            ans += length
        return ans
