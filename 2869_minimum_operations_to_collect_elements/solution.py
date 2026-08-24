# LeetCode 2869 - Minimum Operations to Collect Elements
# https://leetcode.com/problems/minimum-operations-to-collect-elements/

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        need = set(range(1, k + 1))
        for i in range(len(nums) - 1, -1, -1):
            need.discard(nums[i])
            if not need:
                return len(nums) - i
        return len(nums)
