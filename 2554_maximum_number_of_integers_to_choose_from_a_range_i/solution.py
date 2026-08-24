# LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        ans = 0
        s = 0
        for i in range(1, n + 1):
            if i in ban:
                continue
            if s + i > maxSum:
                break
            s += i
            ans += 1
        return ans
