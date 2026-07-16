# LeetCode 0642 - Design Search Autocomplete System
# https://leetcode.com/problems/design-search-autocomplete-system/

from typing import List


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.counts: dict[str, int] = {}
        for sentence, count in zip(sentences, times):
            self.counts[sentence] = self.counts.get(sentence, 0) + count
        self.current = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.counts[self.current] = self.counts.get(self.current, 0) + 1
            self.current = ""
            return []

        self.current += c
        matches = [
            sentence
            for sentence in self.counts
            if sentence.startswith(self.current)
        ]
        matches.sort(key=lambda s: (-self.counts[s], s))
        return matches[:3]
