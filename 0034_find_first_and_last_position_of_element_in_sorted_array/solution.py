# LeetCode 0034 - Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound() -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_bound() -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        if not nums:
            return [-1, -1]

        start = lower_bound()
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, upper_bound() - 1]
