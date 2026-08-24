# LeetCode 3360 - Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/


class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        alice = True
        while n >= take and take > 0:
            n -= take
            take -= 1
            alice = not alice
        return not alice
