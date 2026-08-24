# LeetCode 2185 - Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for w in words:
            if len(w) >= len(pref) and w.startswith(pref):
                ans += 1
        return ans
