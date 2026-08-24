# LeetCode 3566 - Partition Array into Two Equal Product Subsets
# https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range(1 << n):
            x = y = 1
            for j in range(n):
                if ((i >> j) & 1) != 0:
                    x *= nums[j]
                else:
                    y *= nums[j]
                if x > target or y > target:
                    break
            if x == target and y == target:
                return True
        return False
