# LeetCode 0724 - Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            left += num
        return -1
