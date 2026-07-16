# LeetCode 0011 - Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            width = right - left
            best = max(best, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
