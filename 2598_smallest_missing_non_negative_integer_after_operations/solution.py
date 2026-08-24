# LeetCode 2598 - Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for x in nums:
            r = x % value
            if r < 0:
                r += value
            cnt[r] += 1
        mex = 0
        while cnt[mex % value] > 0:
            cnt[mex % value] -= 1
            mex += 1
        return mex
