# LeetCode 0791 - Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        parts: list[str] = []
        for ch in order:
            if counts[ch]:
                parts.append(ch * counts[ch])
                counts[ch] = 0
        for ch, count in counts.items():
            if count:
                parts.append(ch * count)
        return "".join(parts)
