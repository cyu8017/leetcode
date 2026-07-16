# LeetCode 0336 - Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = {word: index for index, word in enumerate(words)}
        result: set[tuple[int, int]] = set()

        for index, word in enumerate(words):
            for split in range(len(word) + 1):
                left, right = word[:split], word[split:]
                if left == left[::-1]:
                    reversed_right = right[::-1]
                    if reversed_right in word_map and word_map[reversed_right] != index:
                        result.add((word_map[reversed_right], index))
                if right == right[::-1]:
                    reversed_left = left[::-1]
                    if reversed_left in word_map and word_map[reversed_left] != index:
                        result.add((index, word_map[reversed_left]))

        return [list(pair) for pair in result]
