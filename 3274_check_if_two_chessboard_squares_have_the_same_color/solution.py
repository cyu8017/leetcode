# LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1 = (ord(coordinate1[0]) - 97) + (ord(coordinate1[1]) - 49)
        c2 = (ord(coordinate2[0]) - 97) + (ord(coordinate2[1]) - 49)
        return c1 % 2 == c2 % 2
