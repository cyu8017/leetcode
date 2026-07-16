# LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

import bisect


class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        def f(s: str) -> int:
            return s.count(min(s))

        freqs = sorted(f(w) for w in words)
        return [len(freqs) - bisect.bisect_right(freqs, f(q)) for q in queries]
