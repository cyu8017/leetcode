# LeetCode 2575 - Find the Divisibility Array of a String
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = [0] * len(word)
        cur = 0
        for i, ch in enumerate(word):
            cur = (cur * 10 + (ord(ch) - 48)) % m
            if cur == 0:
                ans[i] = 1
        return ans
