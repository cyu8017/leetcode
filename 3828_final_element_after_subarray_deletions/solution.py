# LeetCode 3828 - Final Element After Subarray Deletions
# https://leetcode.com/problems/final-element-after-subarray-deletions/

from typing import List


class Solution:
    def finalElement(self, nums: List[int]) -> int:
        return max(nums[0], nums[-1])
