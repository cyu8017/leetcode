# LeetCode 0422 - Valid Word Square
# https://leetcode.com/problems/valid-word-square/

from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for row, word in enumerate(words):
            for col, char in enumerate(word):
                if col >= len(words) or row >= len(words[col]) or words[col][row] != char:
                    return False
        return True
