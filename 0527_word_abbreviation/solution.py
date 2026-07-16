# LeetCode 0527 - Word Abbreviation
# https://leetcode.com/problems/word-abbreviation/

class Solution:
    def wordsAbbreviation(self, words: list[str]) -> list[str]:
        def abbreviate(word: str, prefix: int) -> str:
            if prefix + 2 >= len(word):
                return word
            middle = len(word) - prefix - 1
            candidate = f"{word[:prefix]}{middle}{word[-1]}"
            return candidate if len(candidate) < len(word) else word

        prefixes = [1] * len(words)
        changed = True
        while changed:
            changed = False
            groups: dict[str, list[int]] = {}
            for index, word in enumerate(words):
                key = abbreviate(word, prefixes[index])
                groups.setdefault(key, []).append(index)
            for indices in groups.values():
                if len(indices) > 1:
                    changed = True
                    for index in indices:
                        prefixes[index] += 1
        return [abbreviate(words[index], prefixes[index]) for index in range(len(words))]
