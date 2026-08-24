// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

object Solution {
  def minPathCost(grid: Array[Array[Int]], moveCost: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var dp = grid(0).clone()
    var r = 0
    while (r < m - 1) {
      val next = Array.fill(n)(Int.MaxValue / 2)
      var c = 0
      while (c < n) {
        val from = grid(r)(c)
        var nc = 0
        while (nc < n) {
          next(nc) = math.min(next(nc), dp(c) + moveCost(from)(nc) + grid(r + 1)(nc))
          nc += 1
        }
        c += 1
      }
      dp = next
      r += 1
    }
    var ans = dp(0)
    var i = 1
    while (i < n) {
      ans = math.min(ans, dp(i))
      i += 1
    }
    ans
  }
}
