// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

object Solution {
  def maxConsistentColumns(grid: Array[Array[Int]], limit: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val dp = new Array[Int](n)
    var ans = 1
    var j = 0
    while (j < n) {
      dp(j) = 1
      var i = 0
      while (i < j) {
        if (dp(i) + 1 > dp(j)) {
          var ok = true
          var r = 0
          while (r < m && ok) {
            val d = math.abs(grid(r)(j) - grid(r)(i))
            if (d > limit) ok = false
            r += 1
          }
          if (ok) dp(j) = dp(i) + 1
        }
        i += 1
      }
      if (dp(j) > ans) ans = dp(j)
      j += 1
    }
    ans
  }
}
