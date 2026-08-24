# LeetCode 3810 - Minimum Operations to Reach Target Array
# https://leetcode.com/problems/minimum-operations-to-reach-target-array/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            if nums[i] != target[i]:
                s.add(nums[i])
        return len(s)
