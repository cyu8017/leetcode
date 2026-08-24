// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

object Solution {
  def longestLine(mat: Array[Array[Int]]): Int = {
    if (mat.isEmpty || mat(0).isEmpty) return 0
    val rows = mat.length
    val cols = mat(0).length
    val dp = Array.ofDim[Int](rows, cols, 4)
    var best = 0
    for (r <- 0 until rows; c <- 0 until cols if mat(r)(c) != 0) {
      dp(r)(c)(0) = (if (c > 0) dp(r)(c - 1)(0) else 0) + 1
      dp(r)(c)(1) = (if (r > 0) dp(r - 1)(c)(1) else 0) + 1
      dp(r)(c)(2) = (if (r > 0 && c > 0) dp(r - 1)(c - 1)(2) else 0) + 1
      dp(r)(c)(3) = (if (r > 0 && c + 1 < cols) dp(r - 1)(c + 1)(3) else 0) + 1
      var d = 0
      while (d < 4) {
        best = math.max(best, dp(r)(c)(d))
        d += 1
      }
    }
    best
  }
}
