# LeetCode 3942 - Minimum Operations To Sort A Permutation
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/

from typing import List


def check(nums: List[int], zero: int, step: int) -> bool:
    n = len(nums)
    for i in range(1, n):
        prev = ((zero + (i - 1) * step) % n + n) % n
        curr = ((zero + i * step) % n + n) % n
        if nums[prev] > nums[curr]:
            return False
    return True


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = 0
        for i in range(n):
            if nums[i] == 0:
                zero = i
                break
        ans = 2147483647
        if check(nums, zero, 1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)
        if check(nums, zero, -1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)
        return -1 if ans == 2147483647 else ans
