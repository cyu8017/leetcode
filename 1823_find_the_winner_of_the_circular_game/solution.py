# LeetCode 1823 - Find the Winner of the Circular Game
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        pos = 0
        for size in range(2, n + 1):
            pos = (pos + k) % size
        return pos + 1
