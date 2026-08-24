// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

object Solution {
  def countIslands(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val dirs = Array(-1, 0, 1, 0, -1)
    def dfs(i: Int, j: Int): Long = {
      var s = grid(i)(j).toLong
      grid(i)(j) = 0
      var d = 0
      while (d < 4) {
        val x = i + dirs(d)
        val y = j + dirs(d + 1)
        if (x >= 0 && x < m && y >= 0 && y < n && grid(x)(y) > 0) s += dfs(x, y)
        d += 1
      }
      s
    }
    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) > 0 && dfs(i, j) % k == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
