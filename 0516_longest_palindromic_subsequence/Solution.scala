// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

object Solution {
  def longestPalindromeSubseq(s: String): Int = {
    val length = s.length
    val dp = Array.ofDim[Int](length, length)
    for (index <- length - 1 to 0 by -1) {
      dp(index)(index) = 1
      for (end <- index + 1 until length) {
        dp(index)(end) = if (s(index) == s(end)) {
          dp(index + 1)(end - 1) + 2
        } else {
          math.max(dp(index + 1)(end), dp(index)(end - 1))
        }
      }
    }
    dp(0)(length - 1)
  }
}
