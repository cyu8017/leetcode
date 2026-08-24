# LeetCode 2909 - Minimum Sum of Mountain Triplets II
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        mn = 1 << 30
        for i in range(n):
            left[i] = mn
            if nums[i] < mn:
                mn = nums[i]
        mn = 1 << 30
        for i in range(n - 1, -1, -1):
            right[i] = mn
            if nums[i] < mn:
                mn = nums[i]
        ans = 1 << 30
        for j in range(1, n - 1):
            if left[j] < nums[j] and right[j] < nums[j]:
                cand = left[j] + nums[j] + right[j]
                if cand < ans:
                    ans = cand
        return -1 if ans == (1 << 30) else ans
