# LeetCode 1812 - Determine Color of a Chessboard Square
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[0]) - ord("a") + 1
        row = int(coordinates[1])
        return (col + row) % 2 == 1
