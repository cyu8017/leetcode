# LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
# https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

from typing import List


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        freq = {}
        ans = 0
        same = 0
        for i in range(n):
            if nums1[i] == nums2[i]:
                same += 1
                freq[nums1[i]] = freq.get(nums1[i], 0) + 1
                ans += i
        max_freq = 0
        max_val = 0
        for key, value in freq.items():
            if value > max_freq:
                max_freq = value
                max_val = key
        need = max_freq * 2 - same
        if need <= 0:
            return ans
        i = 0
        while i < n and need > 0:
            if nums1[i] != nums2[i] and nums1[i] != max_val and nums2[i] != max_val:
                ans += i
                need -= 1
            i += 1
        return -1 if need > 0 else ans
