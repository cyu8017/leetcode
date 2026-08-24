# LeetCode 2221 - Find Triangular Sum of an Array
# https://leetcode.com/problems/find-triangular-sum-of-an-array/

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nxt = [0] * (len(nums) - 1)
            for i in range(len(nxt)):
                nxt[i] = (nums[i] + nums[i + 1]) % 10
            nums = nxt
        return nums[0]
