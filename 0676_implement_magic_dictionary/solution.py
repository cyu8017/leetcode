# LeetCode 0676 - Implement Magic Dictionary
# https://leetcode.com/problems/implement-magic-dictionary/

from typing import List


class MagicDictionary:
    def __init__(self):
        self.words: List[str] = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            if sum(a != b for a, b in zip(word, searchWord)) == 1:
                return True
        return False
