# LeetCode 3674 - Minimum Operations to Equalize Array
# https://leetcode.com/problems/minimum-operations-to-equalize-array/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for x in nums:
            if x != nums[0]:
                return 1
        return 0
