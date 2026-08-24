# LeetCode 3131 - Find the Integer Added to Array I
# https://leetcode.com/problems/find-the-integer-added-to-array-i/

from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min1 = nums1[0]
        min2 = nums2[0]
        for x in nums1:
            min1 = min(min1, x)
        for x in nums2:
            min2 = min(min2, x)
        return min2 - min1
