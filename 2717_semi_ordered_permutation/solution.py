# LeetCode 2717 - Semi-Ordered Permutation
# https://leetcode.com/problems/semi-ordered-permutation/

from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        p1 = pn = 0
        for i, x in enumerate(nums):
            if x == 1:
                p1 = i
            if x == n:
                pn = i
        ans = p1 + (n - 1 - pn)
        if p1 > pn:
            ans -= 1
        return ans
