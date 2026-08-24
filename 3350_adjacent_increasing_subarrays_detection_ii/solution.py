# LeetCode 3350 - Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

from typing import List


def ok(up: List[int], n: int, k: int) -> bool:
    for i in range(n - 2 * k + 1):
        if up[i] >= k and up[i + k] >= k:
            return True
    return False


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        up = [0] * n
        up[n - 1] = 1
        for i in range(n - 2, -1, -1):
            up[i] = up[i + 1] + 1 if nums[i] < nums[i + 1] else 1
        lo, hi = 1, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(up, n, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
