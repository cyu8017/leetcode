# LeetCode 2212 - Maximum Points in an Archery Competition
# https://leetcode.com/problems/maximum-points-in-an-archery-competition/

from typing import List
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bestScore = -1
        best = [0] * (12)
        bob = [0] * (12)
        def dfs(i, remain, score):
            nonlocal bestScore, best
            if i == 12:
                if score > bestScore:
                    bestScore = score
                    best = bob[:]
                    if remain > 0:
                        best[0] += remain
                return
            dfs(i + 1, remain, score)
            need = aliceArrows[i] + 1
            if remain >= need:
                bob[i] = need
                dfs(i + 1, remain - need, score + i)
                bob[i] = 0

        dfs(0, numArrows, 0)
        return best
