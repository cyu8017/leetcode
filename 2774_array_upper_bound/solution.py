# LeetCode 2774 - Array Upper Bound
# https://leetcode.com/problems/array-upper-bound/

from typing import List


class Solution:
    def upperBound(self, arr: List[int], target: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) >> 1
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0 or arr[lo - 1] != target:
            return -1
        return lo - 1
