# LeetCode 2828 - Check if a String Is an Acronym of Words
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i, w in enumerate(words):
            if not w or w[0] != s[i]:
                return False
        return True
