# LeetCode 1872 - Stone Game VIII
# https://leetcode.com/problems/stone-game-viii/

from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(1, n):
            stones[i] += stones[i - 1]

        score = stones[-1]
        for i in range(n - 2, 0, -1):
            score = max(stones[i] - score, score)
        return score
