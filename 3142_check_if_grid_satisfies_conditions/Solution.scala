// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

object Solution {
  def satisfiesConditions(grid: Array[Array[Int]]): Boolean = {
    val m = grid.length
    val n = grid(0).length
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val x = grid(i)(j)
        if (i + 1 < m && x != grid(i + 1)(j)) return false
        if (j + 1 < n && x == grid(i)(j + 1)) return false
        j += 1
      }
      i += 1
    }
    true
  }
}
