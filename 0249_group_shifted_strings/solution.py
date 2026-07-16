# LeetCode 0249 - Group Shifted Strings
# https://leetcode.com/problems/group-shifted-strings/

from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups: dict[tuple[int, ...], list[str]] = {}
        for text in strings:
            if not text:
                key = ()
            else:
                base = ord(text[0])
                key = tuple((ord(char) - base) % 26 for char in text)
            groups.setdefault(key, []).append(text)
        return list(groups.values())
