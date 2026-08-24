// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

object Solution {
  def minFlips(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var cnt1 = 0
    var cnt2 = 0
    for (row <- grid) {
      var j = 0
      while (j < n / 2) {
        if (row(j) != row(n - j - 1)) cnt1 += 1
        j += 1
      }
    }
    var j = 0
    while (j < n) {
      var i = 0
      while (i < m / 2) {
        if (grid(i)(j) != grid(m - i - 1)(j)) cnt2 += 1
        i += 1
      }
      j += 1
    }
    math.min(cnt1, cnt2)
  }
}
