# LeetCode 0411 - Minimum Unique Word Abbreviation
# https://leetcode.com/problems/minimum-unique-word-abbreviation/

from typing import List


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        words = [word for word in dictionary if len(word) == len(target)]
        best_len = len(target) + 1
        result = target

        def matches(word: str, abbr: str) -> bool:
            index = 0
            pointer = 0
            while index < len(word) and pointer < len(abbr):
                if abbr[pointer].isdigit():
                    if abbr[pointer] == "0":
                        return False
                    number = 0
                    while pointer < len(abbr) and abbr[pointer].isdigit():
                        number = number * 10 + int(abbr[pointer])
                        pointer += 1
                    index += number
                else:
                    if word[index] != abbr[pointer]:
                        return False
                    index += 1
                    pointer += 1
            return index == len(word) and pointer == len(abbr)

        def valid(abbr: str) -> bool:
            if not matches(target, abbr):
                return False
            return all(not matches(word, abbr) for word in words)

        def dfs(index: int, parts: list[str], skip: int) -> None:
            nonlocal best_len, result
            if index == len(target):
                abbr = "".join(parts) + (str(skip) if skip else "")
                if valid(abbr):
                    if len(abbr) < best_len or (len(abbr) == best_len and abbr < result):
                        best_len = len(abbr)
                        result = abbr
                return

            dfs(index + 1, parts, skip + 1)

            new_parts = list(parts)
            if skip:
                new_parts.append(str(skip))
            new_parts.append(target[index])
            dfs(index + 1, new_parts, 0)

        dfs(0, [], 0)
        return result
