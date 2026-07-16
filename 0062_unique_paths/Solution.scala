// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

object Solution {
  def uniquePaths(m: Int, n: Int): Int = {
    val row = Array.fill(n)(1)

    var r = 1
    while (r < m) {
      var col = 1
      while (col < n) {
        row(col) += row(col - 1)
        col += 1
      }
      r += 1
    }

    row(n - 1)
  }
}
