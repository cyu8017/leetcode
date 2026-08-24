# LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
# https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

from typing import List


class Solution:
    def maximumMatchingIndices(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = 0
        for shift in range(n):
            cnt = 0
            for i in range(n):
                if nums1[(i - shift + n) % n] == nums2[i]:
                    cnt += 1
            if cnt > ans:
                ans = cnt
        return ans
