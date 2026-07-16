# LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

import bisect


class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return right - left > len(nums) // 2
