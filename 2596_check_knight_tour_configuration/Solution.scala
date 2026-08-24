// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

object Solution {
  def checkValidGrid(grid: Array[Array[Int]]): Boolean = {
    val n = grid.length
    if (grid(0)(0) != 0) return false
    val pos = Array.fill(n * n, 2)(0)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        pos(grid(i)(j))(0) = i
        pos(grid(i)(j))(1) = j
        j += 1
      }
      i += 1
    }
    val dirs = Array(
      Array(1, 2), Array(1, -2), Array(-1, 2), Array(-1, -2),
      Array(2, 1), Array(2, -1), Array(-2, 1), Array(-2, -1)
    )
    var v = 0
    while (v + 1 < n * n) {
      val r = pos(v)(0)
      val c = pos(v)(1)
      var ok = false
      dirs.foreach { d =>
        if (r + d(0) == pos(v + 1)(0) && c + d(1) == pos(v + 1)(1)) ok = true
      }
      if (!ok) return false
      v += 1
    }
    true
  }
}
