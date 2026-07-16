# LeetCode 1510

class Solution:
    def winnerSquareGame(self, n):
        win = [False] * (n + 1)
        for value in range(1, n + 1):
            win[value] = any(not win[value - root * root] for root in range(1, int(value ** .5) + 1))
        return win[n]
