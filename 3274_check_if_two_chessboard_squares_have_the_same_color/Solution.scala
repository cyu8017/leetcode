// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

object Solution {
  def checkTwoChessboards(coordinate1: String, coordinate2: String): Boolean = {
    val c1 = (coordinate1.charAt(0) - 'a') + (coordinate1.charAt(1) - '1')
    val c2 = (coordinate2.charAt(0) - 'a') + (coordinate2.charAt(1) - '1')
    c1 % 2 == c2 % 2
  }
}
