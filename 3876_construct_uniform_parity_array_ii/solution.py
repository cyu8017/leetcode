# LeetCode 3876 - Construct Uniform Parity Array II
# https://leetcode.com/problems/construct-uniform-parity-array-ii/

from typing import List


class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        mn = float("inf")
        for x in nums1:
            if x % 2 == 1 and x < mn:
                mn = x
        for x in nums1:
            if x % 2 == 0 and mn != float("inf") and x < mn:
                return False
        return True
