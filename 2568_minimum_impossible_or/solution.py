# LeetCode 2568 - Minimum Impossible OR
# https://leetcode.com/problems/minimum-impossible-or/

from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        x = 1
        while x in s:
            x <<= 1
        return x
