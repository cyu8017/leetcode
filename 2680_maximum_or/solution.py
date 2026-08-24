# LeetCode 2680 - Maximum OR
# https://leetcode.com/problems/maximum-or/

from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        suf = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] | nums[i]
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] | nums[i]
        ans = 0
        for i in range(n):
            cur = pref[i] | (nums[i] * (2 ** k)) | suf[i + 1]
            if cur > ans:
                ans = cur
        return ans
