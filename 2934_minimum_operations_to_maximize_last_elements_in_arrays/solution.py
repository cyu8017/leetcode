# LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
# https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def calc(a1: List[int], a2: List[int]) -> int:
            n = len(a1)
            ops = 0
            last1, last2 = a1[n - 1], a2[n - 1]
            for i in range(n - 1):
                x, y = a1[i], a2[i]
                if x <= last1 and y <= last2:
                    continue
                if y <= last1 and x <= last2:
                    ops += 1
                    continue
                return 1 << 30
            return ops

        n = len(nums1)
        ans = calc(nums1, nums2)
        t = nums1[n - 1]
        nums1[n - 1] = nums2[n - 1]
        nums2[n - 1] = t
        cand = calc(nums1, nums2) + 1
        if cand < ans:
            ans = cand
        nums2[n - 1] = nums1[n - 1]
        nums1[n - 1] = t
        return -1 if ans >= (1 << 30) else ans
