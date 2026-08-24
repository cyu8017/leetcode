# LeetCode 3011 - Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/

from typing import List


def Popcount(x: int) -> int:
    c = 0
    while x != 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        preMx = 0
        i = 0
        n = len(nums)
        while i < n:
            cnt = Popcount(nums[i])
            j = i + 1
            mi = nums[i]
            mx = nums[i]
            while j < n and Popcount(nums[j]) == cnt:
                mi = min(mi, nums[j])
                mx = max(mx, nums[j])
                j += 1
            if preMx > mi:
                return False
            preMx = mx
            i = j
        return True
