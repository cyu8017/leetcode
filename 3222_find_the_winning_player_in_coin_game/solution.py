# LeetCode 3222 - Find the Winning Player in Coin Game
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        k = min(x // 2, y // 8)
        x -= 2 * k
        y -= 8 * k
        if x > 0 and y >= 4:
            return "Alice"
        return "Bob"
