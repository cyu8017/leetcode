// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

object Solution {
  def longestPalindromeSubseq(s: String): Int = {
    val n = s.length
    val dp = Array.ofDim[Int](n, n, 26)
    for (length <- 2 to n; i <- 0 to n - length) {
      val j = i + length - 1
      for (c <- 0 until 26) {
        dp(i)(j)(c) = math.max(dp(i + 1)(j)(c), dp(i)(j - 1)(c))
      }
      if (s(i) == s(j)) {
        val c = s(i) - 'a'
        var inner = 0
        if (length > 2) {
          for (x <- 0 until 26 if x != c) {
            if (dp(i + 1)(j - 1)(x) > inner) inner = dp(i + 1)(j - 1)(x)
          }
        }
        if (inner + 2 > dp(i)(j)(c)) dp(i)(j)(c) = inner + 2
      }
    }
    dp(0)(n - 1).max
  }
}
