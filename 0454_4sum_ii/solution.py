# LeetCode 0454 - 4Sum II
# https://leetcode.com/problems/4sum-ii/

from collections import Counter


class Solution:
    def fourSumCount(
        self,
        nums1: list[int],
        nums2: list[int],
        nums3: list[int],
        nums4: list[int],
    ) -> int:
        pair_sums: Counter[int] = Counter(a + b for a in nums1 for b in nums2)
        total = 0
        for c in nums3:
            for d in nums4:
                total += pair_sums[-(c + d)]
        return total
