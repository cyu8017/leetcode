# LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = s2 = z1 = z2 = 0
        for v in nums1:
            if v == 0:
                z1 += 1
                s1 += 1
            else:
                s1 += v
        for v in nums2:
            if v == 0:
                z2 += 1
                s2 += 1
            else:
                s2 += v
        if z1 == 0 and s1 < s2:
            return -1
        if z2 == 0 and s2 < s1:
            return -1
        return s1 if s1 > s2 else s2
