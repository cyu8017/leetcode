# LeetCode 0809 - Expressive Words
# https://leetcode.com/problems/expressive-words/

from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def groups(text: str) -> list[tuple[str, int]]:
            result: list[tuple[str, int]] = []
            i = 0
            while i < len(text):
                j = i
                while j < len(text) and text[j] == text[i]:
                    j += 1
                result.append((text[i], j - i))
                i = j
            return result

        target = groups(s)

        def stretchy(word: str) -> bool:
            source = groups(word)
            if len(source) != len(target):
                return False
            for (ch1, c1), (ch2, c2) in zip(source, target):
                if ch1 != ch2:
                    return False
                if c1 > c2 or (c1 != c2 and c2 < 3):
                    return False
            return True

        return sum(1 for word in words if stretchy(word))
