// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution {
    fun checkTwoChessboards(coordinate1: String, coordinate2: String): Boolean {
        var c1 = (coordinate1[0] - 'a') + (coordinate1[1] - '1')
        var c2 = (coordinate2[0] - 'a') + (coordinate2[1] - '1')
        return c1 % 2 == c2 % 2
    }
}
