// LeetCode 2319 - Check if Matrix Is X-Matrix
// https://leetcode.com/problems/check-if-matrix-is-x-matrix/

object Solution {
  def checkXMatrix(grid: Array[Array[Int]]): Boolean = {
    val n = grid.length
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        val diag = i == j || i + j == n - 1
        if (diag) {
          if (grid(i)(j) == 0) return false
        } else if (grid(i)(j) != 0) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
