# LeetCode 3132 - Find the Integer Added to Array II
# https://leetcode.com/problems/find-the-integer-added-to-array-ii/

from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        def ok(x: int) -> bool:
            i = 0
            j = 0
            cnt = 0
            while i < len(nums1) and j < len(nums2):
                if nums2[j] - nums1[i] != x:
                    cnt += 1
                else:
                    j += 1
                i += 1
            return cnt <= 2

        ans = 1 << 30
        for t in range(3):
            x = nums2[0] - nums1[t]
            if ok(x):
                ans = min(ans, x)
        return ans
