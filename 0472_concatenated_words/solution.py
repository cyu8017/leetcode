# LeetCode 0472 - Concatenated Words
# https://leetcode.com/problems/concatenated-words/

from collections import defaultdict


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=len)
        word_set = set(words)
        result: list[str] = []

        def can_form(word: str, dictionary: set[str]) -> bool:
            if not word:
                return True
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True
            for end in range(1, length + 1):
                for start in range(end):
                    if dp[start] and word[start:end] in dictionary:
                        dp[end] = True
                        break
            return dp[length]

        for word in words:
            word_set.discard(word)
            if can_form(word, word_set):
                result.append(word)
            word_set.add(word)

        return result
