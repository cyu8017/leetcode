# LeetCode 1829 - Maximum XOR for Each Query
# https://leetcode.com/problems/maximum-xor-for-each-query/

from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        limit = (1 << maximumBit) - 1
        current = 0
        for num in nums:
            current ^= num

        result: List[int] = []
        for i in range(len(nums) - 1, -1, -1):
            result.append(current ^ limit)
            current ^= nums[i]
        return result
