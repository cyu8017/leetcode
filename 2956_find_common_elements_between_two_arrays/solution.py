# LeetCode 2956 - Find Common Elements Between Two Arrays
# https://leetcode.com/problems/find-common-elements-between-two-arrays/

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        a = sum(1 for v in nums1 if v in s2)
        b = sum(1 for v in nums2 if v in s1)
        return [a, b]
