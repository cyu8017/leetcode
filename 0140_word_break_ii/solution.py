# LeetCode 0140 - Word Break II
# https://leetcode.com/problems/word-break-ii/

from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        @lru_cache(None)
        def dfs(start: int) -> tuple[str, ...]:
            if start == len(s):
                return ("",)
            sentences: list[str] = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word not in words:
                    continue
                for tail in dfs(end):
                    sentences.append(word if not tail else f"{word} {tail}")
            return tuple(sentences)

        return list(dfs(0))
