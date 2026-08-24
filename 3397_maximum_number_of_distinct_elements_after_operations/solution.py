# LeetCode 3397 - Maximum Number of Distinct Elements After Operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ans = 0
        prev = -4503599627370496
        for x in nums:
            cur = x - k
            if cur <= prev:
                cur = prev + 1
            if cur > x + k:
                continue
            ans += 1
            prev = cur
        return ans
