# LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
# https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

from typing import List


def upperBound(a: List[int], target: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def countInv(nums: List[int], k: int, threshold: int) -> bool:
    sorted_arr: List[int] = []
    inv = 0
    for num in nums:
        left = upperBound(sorted_arr, num)
        right = upperBound(sorted_arr, num + threshold)
        inv += right - left
        sorted_arr.insert(upperBound(sorted_arr, num), num)
    return inv >= k


class Solution:
    def minThreshold(self, nums: List[int], k: int) -> int:
        mx = 0
        for v in nums:
            if v > mx:
                mx = v
        l, r = 0, mx + 1
        while l < r:
            m = (l + r) >> 1
            if countInv(nums, k, m):
                r = m
            else:
                l = m + 1
        return -1 if l > mx else l
