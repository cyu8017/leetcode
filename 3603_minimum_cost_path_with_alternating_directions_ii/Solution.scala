// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

object Solution {
  def entry(i: Int, j: Int): Long = 1L * (i + 1) * (j + 1)

  def minCost(m: Int, n: Int, waitCost: Array[Array[Int]]): Long = {
    val INF = Long.MaxValue / 4
    val dp = Array.fill(m, n)(INF)
    dp(0)(0) = entry(0, 0)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (!(i == 0 && j == 0)) {
          if (i > 0) {
            var cand = dp(i - 1)(j) + entry(i, j)
            if (!(i - 1 == 0 && j == 0)) cand += waitCost(i - 1)(j)
            dp(i)(j) = math.min(dp(i)(j), cand)
          }
          if (j > 0) {
            var cand = dp(i)(j - 1) + entry(i, j)
            if (!(i == 0 && j - 1 == 0)) cand += waitCost(i)(j - 1)
            dp(i)(j) = math.min(dp(i)(j), cand)
          }
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)
  }
}
