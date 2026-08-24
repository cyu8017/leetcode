# LeetCode 3862 - Find The Smallest Balanced Index
# https://leetcode.com/problems/find-the-smallest-balanced-index/

from typing import List


class Solution:
    def smallestBalancedIndex(self, nums: List[int]) -> int:
        s = 0
        p = 1
        for x in nums:
            s += x
        for i in range(len(nums) - 1, -1, -1):
            s -= nums[i]
            if s == p:
                return i
            p *= nums[i]
            if p >= s:
                break
        return -1
