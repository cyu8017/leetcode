# LeetCode 2321 - Maximum Score Of Spliced Array
# https://leetcode.com/problems/maximum-score-of-spliced-array/

from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def kadane(a: List[int], b: List[int]) -> int:
            best = cur = s = 0
            for i in range(len(a)):
                s += a[i]
                cur += b[i] - a[i]
                if cur < 0:
                    cur = 0
                best = max(best, cur)
            return s + best

        return max(kadane(nums1, nums2), kadane(nums2, nums1))
