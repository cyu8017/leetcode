# LeetCode 0418 - Sentence Screen Fitting
# https://leetcode.com/problems/sentence-screen-fitting/

from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        count = 0
        index = 0
        total = len(sentence)

        for _ in range(rows):
            col = 0
            while True:
                word = sentence[index]
                needed = len(word) + (1 if col > 0 else 0)
                if col + needed > cols:
                    break
                if col > 0:
                    col += 1
                col += len(word)
                index = (index + 1) % total
                if index == 0:
                    count += 1

        return count
