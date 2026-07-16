# LeetCode 0446 - Arithmetic Slices II - Subsequence
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total = 0
        differences: list[defaultdict[int, int]] = [defaultdict(int) for _ in nums]

        for index, value in enumerate(nums):
            for previous in range(index):
                diff = value - nums[previous]
                total += differences[previous][diff]
                differences[index][diff] += differences[previous][diff] + 1

        return total
