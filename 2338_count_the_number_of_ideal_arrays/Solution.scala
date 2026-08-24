// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

object Solution {
  def idealArrays(n: Int, maxValue: Int): Int = {
    val mod = 1000000007
    val maxLen = 14
    val comb = Array.ofDim[Int](n + 1, maxLen + 1)
    var i = 0
    while (i <= n) {
      comb(i)(0) = 1
      var j = 1
      while (j <= maxLen && j <= i) {
        comb(i)(j) = (comb(i - 1)(j) + comb(i - 1)(j - 1)) % mod
        j += 1
      }
      i += 1
    }
    val dp = Array.ofDim[Int](maxValue + 1, maxLen + 1)
    i = 1
    while (i <= maxValue) {
      dp(i)(1) = 1
      i += 1
    }
    var len = 2
    while (len <= maxLen) {
      var v = 1
      while (v <= maxValue) {
        var m = 2 * v
        while (m <= maxValue) {
          dp(m)(len) = (dp(m)(len) + dp(v)(len - 1)) % mod
          m += v
        }
        v += 1
      }
      len += 1
    }
    var ans = 0
    var v = 1
    while (v <= maxValue) {
      len = 1
      while (len <= maxLen && len <= n) {
        ans = (ans + (dp(v)(len).toLong * comb(n - 1)(len - 1) % mod).toInt) % mod
        len += 1
      }
      v += 1
    }
    ans
  }
}
