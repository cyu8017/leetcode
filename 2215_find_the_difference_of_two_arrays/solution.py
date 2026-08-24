# LeetCode 2215 - Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        a = []
        b = []
        for x in s1:
            if x not in s2:
                a.append(x)
        for x in s2:
            if x not in s1:
                b.append(x)
        return [a, b]
