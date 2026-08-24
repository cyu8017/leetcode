// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

object Solution {
  def reverseSubmatrix(grid: Array[Array[Int]], x: Int, y: Int, k: Int): Array[Array[Int]] = {
    var i = x
    while (i < x + k / 2) {
      val i2 = x + k - 1 - (i - x)
      var j = y
      while (j < y + k) {
        val tmp = grid(i)(j)
        grid(i)(j) = grid(i2)(j)
        grid(i2)(j) = tmp
        j += 1
      }
      i += 1
    }
    grid
  }
}
