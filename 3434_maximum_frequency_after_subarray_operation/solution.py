# LeetCode 3434 - Maximum Frequency After Subarray Operation
# https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = 0
        for x in nums:
            if x == k:
                base += 1
        ans = base
        uniq = set(nums)
        for v in uniq:
            if v == k:
                continue
            best = cur = 0
            for x in nums:
                delta = 0
                if x == v:
                    delta = 1
                elif x == k:
                    delta = -1
                cur += delta
                if cur < 0:
                    cur = 0
                if cur > best:
                    best = cur
            if base + best > ans:
                ans = base + best
        return ans
