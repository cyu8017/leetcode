# LeetCode 3909 - Compare Sums Of Bitonic Parts
# https://leetcode.com/problems/compare-sums-of-bitonic-parts/

from typing import List


class Solution:
    def compareBitonicSums(self, nums: List[int]) -> int:
        l = nums[0]
        r = 0
        for x in nums:
            r += x
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                break
            l += nums[i]
            r -= nums[i - 1]
        if l == r:
            return -1
        if l > r:
            return 0
        return 1
