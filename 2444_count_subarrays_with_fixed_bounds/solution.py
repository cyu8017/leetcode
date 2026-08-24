# LeetCode 2444 - Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        imin = imax = ibad = -1
        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                ibad = i
            if x == minK:
                imin = i
            if x == maxK:
                imax = i
            bound = imin if imin < imax else imax
            if bound > ibad:
                ans += bound - ibad
        return ans
