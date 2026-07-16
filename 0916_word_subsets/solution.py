# LeetCode 0916 - Word Subsets
# https://leetcode.com/problems/word-subsets/

from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        need: Counter[str] = Counter()
        for w in words2:
            need |= Counter(w)
        ans = []
        for w in words1:
            if all(Counter(w)[ch] >= need[ch] for ch in need):
                ans.append(w)
        return ans
