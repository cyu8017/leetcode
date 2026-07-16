# LeetCode 1002 - Find Common Characters
# https://leetcode.com/problems/find-common-characters/

from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])
        for w in words[1:]:
            common &= Counter(w)
        return list(common.elements())
