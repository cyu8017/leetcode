// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

object Solution {
  def maxSum(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0
    var i = 0
    while (i + 2 < m) {
      var j = 0
      while (j + 2 < n) {
        val s = grid(i)(j) + grid(i)(j + 1) + grid(i)(j + 2) +
          grid(i + 1)(j + 1) +
          grid(i + 2)(j) + grid(i + 2)(j + 1) + grid(i + 2)(j + 2)
        if (s > ans) ans = s
        j += 1
      }
      i += 1
    }
    ans
  }
}
