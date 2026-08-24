# LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        v = 0
        for raw in nums:
            x = raw ^ v
            if x == 0:
                v ^= 1
                ans += 1
        return ans
