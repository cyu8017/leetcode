# LeetCode 3002 - Maximum Size of a Set After Removals
# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        a = 0
        b = 0
        c = 0
        for x in s1:
            if x not in s2:
                a += 1
        for x in s2:
            if x not in s1:
                b += 1
            else:
                c += 1
        n = len(nums1)
        a = min(a, n // 2)
        b = min(b, n // 2)
        return min(a + b + c, n)
