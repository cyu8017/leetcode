# LeetCode 1121 - Divide Array Into Increasing Sequences
# https://leetcode.com/problems/divide-array-into-increasing-sequences/

from collections import Counter


class Solution:
    def canDivideIntoSubsequences(self, nums: list[int], k: int) -> bool:
        return len(nums) >= k * max(Counter(nums).values())
