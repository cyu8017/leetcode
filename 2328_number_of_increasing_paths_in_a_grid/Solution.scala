// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

object Solution {
  def countPaths(grid: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val m = grid.length
    val n = grid(0).length
    val dp = Array.ofDim[Int](m, n)
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))

    def dfs(r: Int, c: Int): Int = {
      if (dp(r)(c) != 0) return dp(r)(c)
      var res = 1
      dirs.foreach { d =>
        val nr = r + d(0)
        val nc = c + d(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) > grid(r)(c)) {
          res = (res + dfs(nr, nc)) % MOD
        }
      }
      dp(r)(c) = res
      res
    }

    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        ans = (ans + dfs(i, j)) % MOD
        j += 1
      }
      i += 1
    }
    ans
  }
}
