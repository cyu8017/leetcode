# LeetCode 3021 - Alice and Bob Playing Flower Game
# https://leetcode.com/problems/alice-and-bob-playing-flower-game/


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        a1 = (n + 1) // 2
        b1 = (m + 1) // 2
        a2 = n // 2
        b2 = m // 2
        return a1 * b2 + a2 * b1
