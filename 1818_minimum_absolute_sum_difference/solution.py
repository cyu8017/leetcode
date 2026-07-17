# LeetCode 1818 - Minimum Absolute Sum Difference
# https://leetcode.com/problems/minimum-absolute-sum-difference/

import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        sorted_nums1 = sorted(nums1)
        total = sum(abs(a - b) for a, b in zip(nums1, nums2))
        best_gain = 0

        for i, target in enumerate(nums2):
            current = abs(nums1[i] - target)
            idx = bisect.bisect_left(sorted_nums1, target)
            for j in (idx - 1, idx):
                if 0 <= j < len(sorted_nums1):
                    best_gain = max(best_gain, current - abs(sorted_nums1[j] - target))

        return (total - best_gain) % mod
