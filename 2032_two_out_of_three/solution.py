# LeetCode 2032 - Two Out of Three
# https://leetcode.com/problems/two-out-of-three/

from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s0, s1, s2 = set(nums1), set(nums2), set(nums3)
        ans = []
        for v in range(1, 101):
            c = (v in s0) + (v in s1) + (v in s2)
            if c >= 2:
                ans.append(v)
        return ans
