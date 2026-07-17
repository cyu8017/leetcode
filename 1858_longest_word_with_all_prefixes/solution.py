# LeetCode 1858 - Longest Word With All Prefixes
# https://leetcode.com/problems/longest-word-with-all-prefixes/

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        best = ""

        for word in words:
            prefix = word
            valid = True
            while prefix:
                if prefix not in word_set:
                    valid = False
                    break
                prefix = prefix[:-1]

            if valid and (len(word) > len(best) or (len(word) == len(best) and word < best)):
                best = word

        return best
