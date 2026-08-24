// LeetCode 2128 - Remove All Ones With Row and Column Flips
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

object Solution {
  def removeOnes(grid: Array[Array[Int]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    var i = 1
    while (i < m) {
      val same = grid(i)(0) == grid(0)(0)
      var j = 0
      while (j < n) {
        if ((grid(i)(j) == grid(0)(j)) != same) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
