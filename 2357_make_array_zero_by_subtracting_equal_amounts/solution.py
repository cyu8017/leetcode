# LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x > 0:
                seen.add(x)
        return len(seen)
