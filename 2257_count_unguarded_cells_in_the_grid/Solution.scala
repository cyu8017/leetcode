// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

object Solution {
  def countUnguarded(m: Int, n: Int, guards: Array[Array[Int]], walls: Array[Array[Int]]): Int = {
    val grid = Array.ofDim[Int](m, n)
    for (w <- walls) grid(w(0))(w(1)) = 2
    for (g <- guards) grid(g(0))(g(1)) = 2
    val dirs = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))
    for (g <- guards) {
      for (d <- dirs) {
        var r = g(0) + d(0)
        var c = g(1) + d(1)
        while (r >= 0 && r < m && c >= 0 && c < n && grid(r)(c) != 2) {
          grid(r)(c) = 1
          r += d(0)
          c += d(1)
        }
      }
    }
    var ans = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 0) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
