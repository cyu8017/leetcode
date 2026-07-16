# LeetCode 0416 - Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        possible = {0}

        for value in nums:
            possible = possible | {amount + value for amount in possible if amount + value <= target}
            if target in possible:
                return True

        return target in possible
