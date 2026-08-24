# LeetCode 3795 - Minimum Subarray Length with Distinct Sum at Least K
# https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

from typing import List


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = n + 1
        l = 0
        cnt = {}
        s = 0
        for r in range(n):
            c = cnt.get(nums[r], 0) + 1
            cnt[nums[r]] = c
            if c == 1:
                s += nums[r]
            while s >= k:
                if r - l + 1 < ans:
                    ans = r - l + 1
                left = nums[l]
                nc = cnt[left] - 1
                if nc == 0:
                    del cnt[left]
                    s -= left
                else:
                    cnt[left] = nc
                l += 1
        return -1 if ans > n else ans
