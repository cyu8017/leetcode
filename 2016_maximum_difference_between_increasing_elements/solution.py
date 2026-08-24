# LeetCode 2016 - Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        mn = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > mn:
                ans = max(ans, nums[i] - mn)
            else:
                mn = nums[i]
        return ans
