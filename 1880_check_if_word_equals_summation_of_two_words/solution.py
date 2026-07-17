# LeetCode 1880 - Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def _value(self, word: str) -> int:
        return int("".join(str(ord(ch) - ord("a")) for ch in word))

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self._value(firstWord) + self._value(secondWord) == self._value(targetWord)
