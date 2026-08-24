# LeetCode 2744 - Find Maximum Number of String Pairs
# https://leetcode.com/problems/find-maximum-number-of-string-pairs/

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        freq = {}
        ans = 0
        for w in words:
            rev = w[::-1]
            c = freq.get(rev, 0)
            if c > 0:
                ans += 1
                freq[rev] = c - 1
            else:
                freq[w] = freq.get(w, 0) + 1
        return ans
