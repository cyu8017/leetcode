# LeetCode 3496 - Maximize Score After Pair Deletions
# https://leetcode.com/problems/maximize-score-after-pair-deletions/

from typing import List


class Solution:
    def maximizeScore(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for x in nums:
            total += x
        if n % 2 == 1:
            mn = nums[0]
            for x in nums:
                if x < mn:
                    mn = x
            return total - mn
        mn = nums[0] + nums[1]
        for i in range(n - 1):
            mn = min(mn, nums[i] + nums[i + 1])
        return total - mn
