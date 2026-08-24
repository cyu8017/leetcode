# LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

from typing import List


def lowerBound(a: List[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upperBound(a: List[int], x: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = 1
        for t, f in freq.items():
            lo = lowerBound(nums, t - k)
            hi = upperBound(nums, t + k)
            can = hi - lo
            use = min(can, f + numOperations)
            if use > ans:
                ans = use
        l = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            window = min(r - l + 1, numOperations)
            if window > ans:
                ans = window
        return ans
