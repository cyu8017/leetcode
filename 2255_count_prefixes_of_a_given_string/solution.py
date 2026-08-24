# LeetCode 2255 - Count Prefixes of a Given String
# https://leetcode.com/problems/count-prefixes-of-a-given-string/

from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for w in words:
            if len(w) <= len(s) and s.startswith(w):
                ans += 1
        return ans
