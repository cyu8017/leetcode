// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

object Solution {
  def uniquePathsIII(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var empty = 0
    var sr = 0
    var sc = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) != -1) empty += 1
        if (grid(i)(j) == 1) { sr = i; sc = j }
        j += 1
      }
      i += 1
    }
    var ans = 0
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    def dfs(r: Int, c: Int, remain: Int): Unit = {
      if (grid(r)(c) == 2) {
        if (remain == 1) ans += 1
        return
      }
      val temp = grid(r)(c)
      grid(r)(c) = -1
      dirs.foreach { case (dr, dc) =>
        val nr = r + dr
        val nc = c + dc
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr)(nc) != -1) dfs(nr, nc, remain - 1)
      }
      grid(r)(c) = temp
    }
    dfs(sr, sc, empty)
    ans
  }
}
