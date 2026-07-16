# LeetCode 0540 - Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
