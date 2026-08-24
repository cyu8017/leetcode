# LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
# https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

from typing import List


def f3555(nums: List[int], i: int, j: int, inf: int) -> int:
    mi, mx = inf, -inf
    l, r = -1, -1
    for p in range(i, j + 1):
        if nums[p] < mx:
            r = p
        else:
            mx = nums[p]
        q = j - p + i
        if nums[q] > mi:
            l = q
        else:
            mi = nums[q]
    if r == -1:
        return 0
    return r - l + 1


class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        inf = 1 << 30
        n = len(nums)
        return [f3555(nums, i, i + k - 1, inf) for i in range(n - k + 1)]
