// LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

object Solution {
  def minimumDeleteSum(s1: String, s2: String): Int = {
    val m = s1.length
    val n = s2.length
    val dp = Array.ofDim[Int](m + 1, n + 1)
    var i = 1
    while (i <= m) {
      dp(i)(0) = dp(i - 1)(0) + s1.charAt(i - 1)
      i += 1
    }
    var j = 1
    while (j <= n) {
      dp(0)(j) = dp(0)(j - 1) + s2.charAt(j - 1)
      j += 1
    }
    i = 1
    while (i <= m) {
      j = 1
      while (j <= n) {
        if (s1.charAt(i - 1) == s2.charAt(j - 1)) dp(i)(j) = dp(i - 1)(j - 1)
        else dp(i)(j) = math.min(dp(i - 1)(j) + s1.charAt(i - 1), dp(i)(j - 1) + s2.charAt(j - 1))
        j += 1
      }
      i += 1
    }
    dp(m)(n)
  }
}
