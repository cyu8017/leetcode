# LeetCode 0267 - Palindrome Permutation II
# https://leetcode.com/problems/palindrome-permutation-ii/

from collections import Counter
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counts = Counter(s)
        odd_chars = [char for char, count in counts.items() if count % 2]
        if len(odd_chars) > 1:
            return []

        middle = odd_chars[0] if odd_chars else ""
        half: list[str] = []
        for char in sorted(counts):
            half.extend([char] * (counts[char] // 2))

        result: list[str] = []
        used = [False] * len(half)
        path: list[str] = []

        def backtrack() -> None:
            if len(path) == len(half):
                prefix = "".join(path)
                result.append(prefix + middle + prefix[::-1])
                return
            for index, char in enumerate(half):
                if used[index]:
                    continue
                if index > 0 and half[index] == half[index - 1] and not used[index - 1]:
                    continue
                used[index] = True
                path.append(char)
                backtrack()
                path.pop()
                used[index] = False

        backtrack()
        return result
