// LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

object Solution {
  def minFlips(grid: Array[Array[Int]]): Int = {
    val m = grid.length
    val n = grid(0).length
    var ans = 0
    var i = 0
    while (i < m / 2) {
      var j = 0
      while (j < n / 2) {
        val x = m - i - 1
        val y = n - j - 1
        val cnt1 = grid(i)(j) + grid(x)(j) + grid(i)(y) + grid(x)(y)
        ans += math.min(cnt1, 4 - cnt1)
        j += 1
      }
      i += 1
    }
    if (m % 2 == 1 && n % 2 == 1) ans += grid(m / 2)(n / 2)
    var diff = 0
    var ones = 0
    if (m % 2 == 1) {
      var j = 0
      while (j < n / 2) {
        if (grid(m / 2)(j) == grid(m / 2)(n - j - 1)) ones += grid(m / 2)(j) * 2
        else diff += 1
        j += 1
      }
    }
    if (n % 2 == 1) {
      i = 0
      while (i < m / 2) {
        if (grid(i)(n / 2) == grid(m - i - 1)(n / 2)) ones += grid(i)(n / 2) * 2
        else diff += 1
        i += 1
      }
    }
    if (ones % 4 == 0 || diff > 0) ans += diff else ans += 2
    ans
  }
}
