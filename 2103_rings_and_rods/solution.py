# LeetCode 2103 - Rings and Rods
# https://leetcode.com/problems/rings-and-rods/


class Solution:
    def countPoints(self, rings: str) -> int:
        mask = [0] * 10
        for i in range(0, len(rings), 2):
            c = rings[i]
            r = ord(rings[i + 1]) - 48
            bit = 1 if c == "R" else 2 if c == "G" else 4
            mask[r] |= bit
        return sum(1 for m in mask if m == 7)
