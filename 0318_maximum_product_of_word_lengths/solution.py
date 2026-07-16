# LeetCode 0318 - Maximum Product of Word Lengths
# https://leetcode.com/problems/maximum-product-of-word-lengths/

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks: list[int] = []
        lengths: list[int] = []
        for word in words:
            mask = 0
            valid = True
            for char in word:
                bit = 1 << (ord(char) - ord("a"))
                if mask & bit:
                    valid = False
                    break
                mask |= bit
            masks.append(0 if not valid else mask)
            lengths.append(len(word))
        best = 0
        for left in range(len(words)):
            if masks[left] == 0:
                continue
            for right in range(left + 1, len(words)):
                if masks[right] == 0:
                    continue
                if masks[left] & masks[right] == 0:
                    best = max(best, lengths[left] * lengths[right])
        return best
