# LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
# https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

from typing import Dict, List


class Solution:
    def minCost(self, nums1: List[int], nums2: List[int]) -> int:
        cnt2: Dict[int, int] = {}
        for x in nums2:
            cnt2[x] = cnt2.get(x, 0) + 1
        cnt1: Dict[int, int] = {}
        for x in nums1:
            c = cnt2.get(x, 0)
            if c > 0:
                cnt2[x] = c - 1
            else:
                cnt1[x] = cnt1.get(x, 0) + 1
        ans = 0
        for v in cnt1.values():
            if v % 2 == 1:
                return -1
            ans += v // 2
        for v in cnt2.values():
            if v % 2 == 1:
                return -1
        return ans
