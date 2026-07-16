# LeetCode 0259 - 3Sum Smaller
# https://leetcode.com/problems/3sum-smaller/

from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        length = len(nums)
        for index in range(length - 2):
            left = index + 1
            right = length - 1
            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
