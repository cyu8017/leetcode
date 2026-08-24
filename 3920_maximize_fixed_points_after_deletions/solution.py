# LeetCode 3920 - Maximize Fixed Points After Deletions
# https://leetcode.com/problems/maximize-fixed-points-after-deletions/

from typing import List


class Solution:
    def maxFixedPoints(self, nums: List[int]) -> int:
        tails: List[int] = []
        for i in range(len(nums)):
            if i < nums[i]:
                continue
            d = i - nums[i]
            lo = 0
            hi = len(tails)
            while lo < hi:
                mid = (lo + hi) >> 1
                if tails[mid] < d:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(tails):
                tails.append(d)
            else:
                tails[lo] = d
        return len(tails)
