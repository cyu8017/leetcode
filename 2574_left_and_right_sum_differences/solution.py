# LeetCode 2574 - Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        ans = [0] * len(nums)
        left = 0
        for i, x in enumerate(nums):
            right = total - left - x
            ans[i] = abs(left - right)
            left += x
        return ans
