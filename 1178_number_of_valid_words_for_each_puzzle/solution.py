# LeetCode 1178 - Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        def mask_of(s: str) -> int:
            mask = 0
            for ch in s:
                mask |= 1 << (ord(ch) - 97)
            return mask

        freq = Counter(mask_of(w) for w in words)
        ans = []
        for puzzle in puzzles:
            first = 1 << (ord(puzzle[0]) - 97)
            full = mask_of(puzzle)
            sub = full
            total = 0
            while True:
                if sub & first:
                    total += freq[sub]
                if sub == 0:
                    break
                sub = (sub - 1) & full
            ans.append(total)
        return ans
