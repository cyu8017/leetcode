# LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

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
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        ans = 1
        candidates = []
        seen = set()
        for x in nums:
            for t in (x - k, x, x + k):
                if t not in seen:
                    seen.add(t)
                    candidates.append(t)
        for t in candidates:
            lo = lowerBound(nums, t - k)
            hi = upperBound(nums, t + k)
            can = hi - lo
            f = freq.get(t, 0)
            use = min(can, f + numOperations)
            if use > ans:
                ans = use
        return ans
