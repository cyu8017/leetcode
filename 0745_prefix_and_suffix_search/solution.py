# LeetCode 0745 - Prefix and Suffix Search
# https://leetcode.com/problems/prefix-and-suffix-search/

from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        self.lookup: dict[str, int] = {}
        for index, word in enumerate(words):
            size = len(word)
            for i in range(size + 1):
                for j in range(size + 1):
                    self.lookup[word[:i] + "#" + word[j:]] = index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get(pref + "#" + suff, -1)
