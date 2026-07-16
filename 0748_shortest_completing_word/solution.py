# LeetCode 0748 - Shortest Completing Word
# https://leetcode.com/problems/shortest-completing-word/

from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        best = None
        for word in words:
            counts = Counter(word)
            if all(counts[ch] >= cnt for ch, cnt in need.items()):
                if best is None or len(word) < len(best):
                    best = word
        return best or ""
