# LeetCode 2586 - Count the Number of Vowel Strings in Range
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def is_v(c: str) -> bool:
            return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

        ans = 0
        for i in range(left, right + 1):
            w = words[i]
            if is_v(w[0]) and is_v(w[-1]):
                ans += 1
        return ans
