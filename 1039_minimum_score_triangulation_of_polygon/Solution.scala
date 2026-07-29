// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

object Solution {
  def minScoreTriangulation(values: Array[Int]): Int = {
    val n = values.length
    val memo = Array.fill(n, n)(-1)
    def dp(i: Int, j: Int): Int = {
      if (j - i < 2) return 0
      if (memo(i)(j) != -1) return memo(i)(j)
      var best = Int.MaxValue
      for (k <- (i + 1) until j) {
        best = math.min(best, dp(i, k) + values(i) * values(k) * values(j) + dp(k, j))
      }
      memo(i)(j) = best
      best
    }
    dp(0, n - 1)
  }
}
