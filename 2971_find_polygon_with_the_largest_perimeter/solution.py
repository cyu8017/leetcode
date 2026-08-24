# LeetCode 2971 - Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for v in nums:
            total += v
        for i in range(len(nums) - 1, 1, -1):
            total -= nums[i]
            if total > nums[i]:
                return total + nums[i]
        return -1
