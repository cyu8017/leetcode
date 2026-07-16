# LeetCode 0822 - Card Flipping Game
# https://leetcode.com/problems/card-flipping-game/

class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        same = {f for f, b in zip(fronts, backs) if f == b}
        best = float("inf")
        for x in fronts + backs:
            if x not in same:
                best = min(best, x)
        return 0 if best == float("inf") else best
