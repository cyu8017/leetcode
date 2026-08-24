# LeetCode 3035 - Maximum Palindromes After Operations
# https://leetcode.com/problems/maximum-palindromes-after-operations/

from typing import List


def popcount(x: int) -> int:
    c = 0
    while x != 0:
        c += x & 1
        x >>= 1
    return c


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        s = 0
        mask = 0
        for w in words:
            s += len(w)
            for i in range(len(w)):
                mask ^= 1 << (ord(w[i]) - 97)
        s -= popcount(mask)
        words.sort(key=lambda w: len(w))
        ans = 0
        for w in words:
            s -= (len(w) // 2) * 2
            if s < 0:
                break
            ans += 1
        return ans
