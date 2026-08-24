// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

object Solution {
  def minimumOperations(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0
    var j = 0
    while (j < n) {
      var i = 1
      while (i < m) {
        if (grid(i)(j) <= grid(i - 1)(j)) {
          val need = grid(i - 1)(j) + 1
          ans += need - grid(i)(j)
          grid(i)(j) = need
        }
        i += 1
      }
      j += 1
    }
    ans
  }
}
