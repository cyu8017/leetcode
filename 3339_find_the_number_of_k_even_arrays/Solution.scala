// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

object Solution {
  def countOfArrays(n: Int, m: Int, k: Int): Int = {
    val mod = 1000000007
    val even = m / 2
    val odd = m - even
    val dp = Array.ofDim[Int](n + 1, k + 1, 2)
    dp(1)(0)(0) = odd
    dp(1)(0)(1) = even
    var i = 1
    while (i < n) {
      var j = 0
      while (j <= k) {
        dp(i + 1)(j)(0) = (dp(i + 1)(j)(0) + (((dp(i)(j)(0).toLong + dp(i)(j)(1)) % mod) * odd % mod).toInt) % mod
        dp(i + 1)(j)(1) = (dp(i + 1)(j)(1) + (dp(i)(j)(0).toLong * even % mod).toInt) % mod
        if (j < k) {
          dp(i + 1)(j + 1)(1) = (dp(i + 1)(j + 1)(1) + (dp(i)(j)(1).toLong * even % mod).toInt) % mod
        }
        j += 1
      }
      i += 1
    }
    (dp(n)(k)(0) + dp(n)(k)(1)) % mod
  }
}
