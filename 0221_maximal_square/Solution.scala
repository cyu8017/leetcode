// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

object Solution {
  def maximalSquare(matrix: Array[Array[Char]]): Int = {
    if (matrix == null || matrix.length == 0) {
      0
    } else {
      val rows = matrix.length
      val cols = matrix(0).length
      val dp = new Array[Int](cols + 1)
      var maxSide = 0
      var prev = 0
      for (row <- 1 to rows) {
        for (col <- 1 to cols) {
          val temp = dp(col)
          if (matrix(row - 1)(col - 1) == '1') {
            dp(col) = Math.min(dp(col), Math.min(dp(col - 1), prev)) + 1
            maxSide = Math.max(maxSide, dp(col))
          } else {
            dp(col) = 0
          }
          prev = temp
        }
      }
      maxSide * maxSide
    }
  }
}
