# LeetCode 2559 - Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_v(c: str) -> bool:
            return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

        n = len(words)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i]
            w = words[i]
            if len(w) > 0 and is_v(w[0]) and is_v(w[-1]):
                pref[i + 1] += 1
        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            ans[i] = pref[r + 1] - pref[l]
        return ans
