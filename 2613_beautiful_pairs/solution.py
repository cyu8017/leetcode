# LeetCode 2613 - Beautiful Pairs
# https://leetcode.com/problems/beautiful-pairs/

from typing import List


class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        best = float("inf")
        ans = [0, 1]
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(nums1[i] - nums1[j]) + abs(nums2[i] - nums2[j])
                if d < best or (d == best and (i < ans[0] or (i == ans[0] and j < ans[1]))):
                    best = d
                    ans = [i, j]
        return ans
