// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

object Solution {
  def longestCommonSubsequence(text1: String, text2: String): Int = {
    val m = text1.length
    val n = text2.length
    val dp = Array.ofDim[Int](n + 1)
    for (i <- 1 to m) {
      var prev = 0
      for (j <- 1 to n) {
        val cur = dp(j)
        if (text1(i - 1) == text2(j - 1)) dp(j) = prev + 1
        else dp(j) = math.max(dp(j), dp(j - 1))
        prev = cur
      }
    }
    dp(n)
  }
}
