# LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/


class Solution:
    def twoEggDrop(self, n: int) -> int:
        moves = 0
        covered = 0
        while covered < n:
            moves += 1
            covered += moves
        return moves
