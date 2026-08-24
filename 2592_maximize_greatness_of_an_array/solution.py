# LeetCode 2592 - Maximize Greatness of an Array
# https://leetcode.com/problems/maximize-greatness-of-an-array/

from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums:
            if x > nums[i]:
                i += 1
        return i
