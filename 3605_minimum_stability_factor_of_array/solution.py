# LeetCode 3605 - Minimum Stability Factor of Array
# https://leetcode.com/problems/minimum-stability-factor-of-array/

from typing import List


def gcd3605(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def ok3605(nums: List[int], max_c: int, x: int) -> bool:
    n = len(nums)
    if x >= n:
        return True
    changes = 0
    i = 0
    while i + x < n:
        g = nums[i]
        for j in range(i + 1, i + x + 1):
            g = gcd3605(g, nums[j])
        if g > 1:
            changes += 1
            i += x + 1
        else:
            i += 1
    return changes <= max_c


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if ok3605(nums, maxC, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
