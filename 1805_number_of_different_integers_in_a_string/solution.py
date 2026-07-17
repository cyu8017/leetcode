# LeetCode 1805 - Number of Different Integers in a String
# https://leetcode.com/problems/number-of-different-integers-in-a-string/

import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen: set[int] = set()
        for match in re.finditer(r"\d+", word):
            seen.add(int(match.group()))
        return len(seen)
