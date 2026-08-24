// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

object Solution {
  def maxMoves(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var dp = new Array[Int](m)
    var c = n - 2
    while (c >= 0) {
      val ndp = new Array[Int](m)
      var r = 0
      while (r < m) {
        var best = 0
        var dr = -1
        while (dr <= 1) {
          val nr = r + dr
          if (nr >= 0 && nr < m && grid(nr)(c + 1) > grid(r)(c))
            best = math.max(best, 1 + dp(nr))
          dr += 1
        }
        ndp(r) = best
        r += 1
      }
      dp = ndp
      c -= 1
    }
    var ans = 0
    var i = 0
    while (i < dp.length) {
      ans = math.max(ans, dp(i))
      i += 1
    }
    ans
  }
}
