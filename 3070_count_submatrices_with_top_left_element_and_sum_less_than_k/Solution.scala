// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

object Solution {
  def countSubmatrices(grid: Array[Array[Int]], k: Int): Int = {
    val n = grid.length
    val m = grid(0).length
    var ans = 0
    val s = Array.fill(n + 1, m + 1)(0)
    var i = 0
    while (i < n) {
      var j = 0
      while (j < m) {
        s(i + 1)(j + 1) = s(i + 1)(j) + s(i)(j + 1) - s(i)(j) + grid(i)(j)
        if (s(i + 1)(j + 1) <= k) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
