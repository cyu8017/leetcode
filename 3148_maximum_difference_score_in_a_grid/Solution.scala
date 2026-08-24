// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

object Solution {
  def maxScore(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    val INF = 1 << 30
    val f = Array.ofDim[Int](m, n)
    var ans = -INF
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val x = grid(i)(j)
        var mi = INF
        if (i > 0) mi = math.min(mi, f(i - 1)(j))
        if (j > 0) mi = math.min(mi, f(i)(j - 1))
        ans = math.max(ans, x - mi)
        f(i)(j) = math.min(x, mi)
        j += 1
      }
      i += 1
    }
    ans
  }
}
