// LeetCode 3742 - Maximum Path Score In A Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

object Solution {
  private val INF = 1 << 30

  def maxPathScore(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val f = Array.fill(m, n, k + 1)(-1)

    def dfs(i: Int, j: Int, kk: Int): Int = {
      if (i < 0 || j < 0 || kk < 0) return -INF
      if (i == 0 && j == 0) return 0
      if (f(i)(j)(kk) != -1) return f(i)(j)(kk)
      var res = grid(i)(j)
      var nk = kk
      if (grid(i)(j) != 0) nk -= 1
      val a = dfs(i - 1, j, nk)
      val b = dfs(i, j - 1, nk)
      res += math.max(a, b)
      f(i)(j)(kk) = res
      res
    }

    val ans = dfs(m - 1, n - 1, k)
    if (ans < 0) -1 else ans
  }
}
