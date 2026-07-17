# LeetCode 1863 - Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for num in nums:
            bits |= num

        total = 0
        bit = 1
        while bit <= bits:
            if bits & bit:
                total += bit
            bit <<= 1

        return total << (len(nums) - 1)
