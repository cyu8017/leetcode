# LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        b = 100
        c = 100
        for i in range(1, len(nums)):
            x = nums[i]
            if x < b:
                c = b
                b = x
            elif x < c:
                c = x
        return a + b + c
