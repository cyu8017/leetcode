# LeetCode 2505 - Bitwise OR of All Subsequence Sums
# https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

from typing import List


class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0
        for x in nums:
            prefix += x
            ans |= x | prefix
        return ans
