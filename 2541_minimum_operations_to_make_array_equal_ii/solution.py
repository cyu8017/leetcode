# LeetCode 2541 - Minimum Operations to Make Array Equal II
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            for i in range(len(nums1)):
                if nums1[i] != nums2[i]:
                    return -1
            return 0
        pos = 0
        neg = 0
        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            if d % k != 0:
                return -1
            if d > 0:
                pos += d // k
            else:
                neg += (-d) // k
        return -1 if pos != neg else pos
