# LeetCode 3301 - Maximize the Total Height of Unique Towers
# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = 0
        prev = 10**18
        for h in maximumHeight:
            cur = h
            if cur >= prev:
                cur = prev - 1
            if cur <= 0:
                return -1
            ans += cur
            prev = cur
        return ans
