# LeetCode 0288 - Unique Word Abbreviation
# https://leetcode.com/problems/unique-word-abbreviation/


class ValidWordAbbr:
    def __init__(self, dictionary: list[str]):
        self.groups: dict[str, set[str]] = {}
        for word in dictionary:
            key = self._abbreviate(word)
            self.groups.setdefault(key, set()).add(word)

    def isUnique(self, word: str) -> bool:
        key = self._abbreviate(word)
        words = self.groups.get(key, set())
        return not words or (len(words) == 1 and word in words)

    @staticmethod
    def _abbreviate(word: str) -> str:
        if len(word) <= 2:
            return word
        return f"{word[0]}{len(word) - 2}{word[-1]}"
