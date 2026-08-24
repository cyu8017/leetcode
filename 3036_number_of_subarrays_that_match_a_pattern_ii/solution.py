# LeetCode 3036 - Number of Subarrays That Match a Pattern II
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        N = len(pattern)
        ps = [0] * (N + 1)
        ps[0] = -1
        ps[1] = 0
        p = 0
        for i in range(2, N + 1):
            x = pattern[i - 1]
            while p >= 0 and pattern[p] != x:
                p = ps[p]
            p += 1
            ps[i] = p
        res = 0
        M = len(nums)
        p = 0
        for i in range(1, M):
            t = nums[i] - nums[i - 1]
            if t > 0:
                t = 1
            elif t < 0:
                t = -1
            while p >= 0 and pattern[p] != t:
                p = ps[p]
            p += 1
            if p == N:
                res += 1
                p = ps[p]
        return res
