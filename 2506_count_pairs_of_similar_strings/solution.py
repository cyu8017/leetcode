# LeetCode 2506 - Count Pairs Of Similar Strings
# https://leetcode.com/problems/count-pairs-of-similar-strings/

from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = {}
        ans = 0
        for w in words:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - 97)
            ans += freq.get(mask, 0)
            freq[mask] = freq.get(mask, 0) + 1
        return ans
