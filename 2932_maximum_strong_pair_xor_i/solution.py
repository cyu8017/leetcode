# LeetCode 2932 - Maximum Strong Pair XOR I
# https://leetcode.com/problems/maximum-strong-pair-xor-i/

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    xorr = x ^ y
                    if xorr > ans:
                        ans = xorr
        return ans
