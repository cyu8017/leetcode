// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

object Solution {
  def countPathsWithXorValue(grid: Array[Array[Int]], k: Int): Int = {
    val mod = 1000000007
    val m = grid.length
    val n = grid(0).length
    val dp = Array.fill(m, n, 16)(0)
    dp(0)(0)(grid(0)(0)) = 1
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var x = 0
        while (x < 16) {
          if (dp(i)(j)(x) != 0) {
            if (i + 1 < m) {
              val nx = x ^ grid(i + 1)(j)
              dp(i + 1)(j)(nx) = (dp(i + 1)(j)(nx) + dp(i)(j)(x)) % mod
            }
            if (j + 1 < n) {
              val nx = x ^ grid(i)(j + 1)
              dp(i)(j + 1)(nx) = (dp(i)(j + 1)(nx) + dp(i)(j)(x)) % mod
            }
          }
          x += 1
        }
        j += 1
      }
      i += 1
    }
    dp(m - 1)(n - 1)(k)
  }
}
