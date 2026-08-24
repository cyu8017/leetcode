# LeetCode 2439 - Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/

from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        ans = 0
        for i in range(len(nums)):
            total += nums[i]
            avg = (total + i) // (i + 1)
            if avg > ans:
                ans = avg
        return ans
