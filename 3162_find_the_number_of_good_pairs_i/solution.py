# LeetCode 3162 - Find the Number of Good Pairs I
# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for x in nums1:
            for y in nums2:
                if x % (y * k) == 0:
                    ans += 1
        return ans
