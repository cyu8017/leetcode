# LeetCode 0243 - Shortest Word Distance
# https://leetcode.com/problems/shortest-word-distance/

from typing import List


class Solution:
    def shortestWordDistance(
        self, wordsDict: List[str], word1: str, word2: str
    ) -> int:
        index1 = index2 = -1
        best = float("inf")
        for index, word in enumerate(wordsDict):
            if word == word1:
                index1 = index
                if index2 >= 0:
                    best = min(best, index - index2)
            if word == word2:
                index2 = index
                if index1 >= 0:
                    best = min(best, index - index1)
        return int(best)
