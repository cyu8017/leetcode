# LeetCode 2936 - Number of Equal Numbers Blocks
# https://leetcode.com/problems/number-of-equal-numbers-blocks/

from typing import List


class Solution:
    def blockCount(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ans += 1
        return ans
