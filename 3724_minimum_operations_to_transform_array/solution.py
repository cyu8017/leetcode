# LeetCode 3724 - Minimum Operations to Transform Array
# https://leetcode.com/problems/minimum-operations-to-transform-array/

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 1
        n = len(nums1)
        ok = False
        d = 1 << 30
        for i in range(n):
            x = max(nums1[i], nums2[i])
            y = min(nums1[i], nums2[i])
            ans += x - y
            d = min(d, min(abs(x - nums2[n]), abs(y - nums2[n])))
            if nums2[n] >= y and nums2[n] <= x:
                ok = True
        if not ok:
            ans += d
        return ans
