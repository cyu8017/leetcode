# LeetCode 2605 - Form Smallest Number From Two Digit Arrays
# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        common = 10
        for x in s1:
            if x in s2 and x < common:
                common = x
        if common < 10:
            return common
        a = min(nums1)
        b = min(nums2)
        return min(a * 10 + b, b * 10 + a)
