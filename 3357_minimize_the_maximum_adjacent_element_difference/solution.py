# LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
# https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

from typing import List


def ok(d: int, nums: List[int], n: int) -> bool:
    prev = -1
    i = 0
    while i < n:
        if nums[i] != -1:
            if prev != -1 and abs(nums[i] - prev) > d:
                return False
            prev = nums[i]
            i += 1
            continue
        j = i
        while j < n and nums[j] == -1:
            j += 1
        left = prev
        right = nums[j] if j < n else -1
        gap = j - i
        if left == -1 and right == -1:
            return True
        if left == -1 or right == -1:
            prev = -1
            i = j
            continue
        if abs(left - right) > d * (gap + 1):
            return False
        prev = -1
        i = j
    return True


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, 1000000000
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid, nums, n):
                hi = mid
            else:
                lo = mid + 1
        return lo
