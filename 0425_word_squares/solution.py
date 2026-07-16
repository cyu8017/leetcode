# LeetCode 0425 - Word Squares
# https://leetcode.com/problems/word-squares/

from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        words.sort()
        length = len(words[0])
        prefix_map: dict[str, list[str]] = {"": words[:]}
        for word in words:
            for index in range(len(word)):
                prefix = word[: index + 1]
                prefix_map.setdefault(prefix, []).append(word)

        squares: list[list[str]] = []
        current: list[str] = []

        def dfs(row: int) -> None:
            if row == length:
                squares.append(current.copy())
                return
            prefix = "".join(word[row] for word in current)
            for candidate in prefix_map.get(prefix, []):
                current.append(candidate)
                dfs(row + 1)
                current.pop()

        dfs(0)
        return squares
