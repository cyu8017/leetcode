# LeetCode 0320 - Generalized Abbreviation
# https://leetcode.com/problems/generalized-abbreviation/

from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result: list[str] = []

        def backtrack(index: int, path: str, count: int) -> None:
            if index == len(word):
                result.append(path + (str(count) if count else ""))
                return
            backtrack(index + 1, path, count + 1)
            next_path = path + (str(count) if count else "") + word[index]
            backtrack(index + 1, next_path, 0)

        backtrack(0, "", 0)
        return result
