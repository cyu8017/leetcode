# LeetCode 0213 - House Robber II
# https://leetcode.com/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            prev2 = prev1 = 0
            for num in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
