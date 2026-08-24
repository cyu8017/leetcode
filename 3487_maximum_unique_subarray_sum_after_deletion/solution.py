# LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        s = 0
        has_pos = False
        max_neg = -10**9
        for x in nums:
            if x < 0:
                if x > max_neg:
                    max_neg = x
                continue
            has_pos = True
            if x not in seen:
                seen.add(x)
                s += x
        return s if has_pos else max_neg
