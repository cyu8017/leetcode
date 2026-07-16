# LeetCode 0268 - Missing Number
# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        expected = length * (length + 1) // 2
        return expected - sum(nums)
