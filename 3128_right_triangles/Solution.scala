// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

object Solution {
  def numberOfRightTriangles(grid: Array[Array[Int]]): Long = {
    val m = grid.length
    val n = grid(0).length
    val rows = new Array[Int](m)
    val cols = new Array[Int](n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        rows(i) += grid(i)(j)
        cols(j) += grid(i)(j)
        j += 1
      }
      i += 1
    }
    var ans = 0L
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (grid(i)(j) == 1) ans += (rows(i) - 1).toLong * (cols(j) - 1)
        j += 1
      }
      i += 1
    }
    ans
  }
}
