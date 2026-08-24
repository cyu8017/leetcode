# LeetCode 2935 - Maximum Strong Pair XOR II
# https://leetcode.com/problems/maximum-strong-pair-xor-ii/

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        for i, x in enumerate(nums):
            j = i
            while j < len(nums) and nums[j] <= 2 * x:
                xorr = x ^ nums[j]
                if xorr > ans:
                    ans = xorr
                j += 1
        return ans
