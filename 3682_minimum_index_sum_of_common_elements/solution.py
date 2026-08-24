# LeetCode 3682 - Minimum Index Sum of Common Elements
# https://leetcode.com/problems/minimum-index-sum-of-common-elements/

from typing import List


class Solution:
    def minimumSum(self, nums1: List[int], nums2: List[int]) -> int:
        inf = 1 << 30
        d = {}
        for i, x in enumerate(nums2):
            if x not in d:
                d[x] = i
        ans = inf
        for i, x in enumerate(nums1):
            if x in d:
                ans = min(ans, i + d[x])
        return -1 if ans == inf else ans
