# LeetCode 1160 - Find Words That Can Be Formed by Characters
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        avail = Counter(chars)
        ans = 0
        for word in words:
            need = Counter(word)
            if all(need[c] <= avail[c] for c in need):
                ans += len(word)
        return ans
