// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

object Solution {
  def countPalindromicSubsequences(s: String): Int = {
    val mod = 1000000007
    val n = s.length
    val dp = Array.ofDim[Long](n, n)
    var i = 0
    while (i < n) {
      dp(i)(i) = 1
      i += 1
    }
    var length = 2
    while (length <= n) {
      i = 0
      while (i <= n - length) {
        val j = i + length - 1
        if (s.charAt(i) != s.charAt(j)) dp(i)(j) = dp(i + 1)(j) + dp(i)(j - 1) - dp(i + 1)(j - 1)
        else {
          var left = i + 1
          var right = j - 1
          while (left <= right && s.charAt(left) != s.charAt(i)) left += 1
          while (left <= right && s.charAt(right) != s.charAt(i)) right -= 1
          if (left > right) dp(i)(j) = dp(i + 1)(j - 1) * 2 + 2
          else if (left == right) dp(i)(j) = dp(i + 1)(j - 1) * 2 + 1
          else dp(i)(j) = dp(i + 1)(j - 1) * 2 - dp(left + 1)(right - 1)
        }
        dp(i)(j) = (dp(i)(j) % mod + mod) % mod
        i += 1
      }
      length += 1
    }
    dp(0)(n - 1).toInt
  }
}
