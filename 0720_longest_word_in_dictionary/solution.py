# LeetCode 0720 - Longest Word in Dictionary
# https://leetcode.com/problems/longest-word-in-dictionary/

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        built = {""}
        best = ""
        for word in words:
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(best):
                    best = word
        return best
