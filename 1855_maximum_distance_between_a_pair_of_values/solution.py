# LeetCode 1855 - Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0
        j = 0

        for i, value in enumerate(nums1):
            while j < len(nums2) and value <= nums2[j]:
                j += 1
            answer = max(answer, j - i - 1)

        return answer
