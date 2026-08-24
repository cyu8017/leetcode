# LeetCode 3523 - Make Array Non-decreasing
# https://leetcode.com/problems/make-array-non-decreasing/

from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = 0
        mx = 0
        for x in nums:
            if mx <= x:
                ans += 1
                mx = x
        return ans
