# LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap = [n] * n
        keep = [n] * n
        swap[0], keep[0] = 1, 0
        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        return min(swap[-1], keep[-1])
