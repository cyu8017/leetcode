# LeetCode 3968 - Maximum Manhattan Distance After All Moves
# https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/


class Solution:
    def maxDistance(self, moves: str) -> int:
        x = 0
        y = 0
        z = 0
        for i in range(len(moves)):
            c = moves[i]
            if c == "U":
                x -= 1
            elif c == "D":
                x += 1
            elif c == "L":
                y -= 1
            elif c == "R":
                y += 1
            else:
                z += 1
        return abs(x) + abs(y) + z
