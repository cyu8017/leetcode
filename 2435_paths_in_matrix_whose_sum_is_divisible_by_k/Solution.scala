// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

object Solution {
  def numberOfPaths(grid: Array[Array[Int]], k: Int): Int = {
    val mod = 1000000007
    val m = grid.length
    val n = grid(0).length
    val dp = Array.ofDim[Int](m, n, k)
    dp(0)(0)(grid(0)(0) % k) = 1
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var r = 0
        while (r < k) {
          if (dp(i)(j)(r) != 0) {
            if (i + 1 < m) {
              val nr = (r + grid(i + 1)(j)) % k
              dp(i + 1)(j)(nr) = (dp(i + 1)(j)(nr) + dp(i)(j)(r)) % mod
            }
            if (j + 1 < n) {
              val nr = (r + grid(i)(j + 1)) % k
              dp(i)(j + 1)(nr) = (dp(i)(j + 1)(nr) + dp(i)(j)(r)) % mod
            }
          }
          r += 1
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)(0)
  }
}
