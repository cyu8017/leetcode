# LeetCode 0648 - Replace Words
# https://leetcode.com/problems/replace-words/

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)

        def replace(word: str) -> str:
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    return prefix
            return word

        return " ".join(replace(word) for word in sentence.split())
