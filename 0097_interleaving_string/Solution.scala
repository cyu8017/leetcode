// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

object Solution {
  def isInterleave(s1: String, s2: String, s3: String): Boolean = {
    if (s1.length + s2.length != s3.length) {
      return false
    }

    val m = s1.length
    val n = s2.length
    val dp = Array.fill(n + 1)(false)
    dp(0) = true

    for (j <- 1 to n) {
      dp(j) = dp(j - 1) && s2.charAt(j - 1) == s3.charAt(j - 1)
    }

    for (i <- 1 to m) {
      dp(0) = dp(0) && s1.charAt(i - 1) == s3.charAt(i - 1)
      for (j <- 1 to n) {
        dp(j) = (dp(j) && s1.charAt(i - 1) == s3.charAt(i + j - 1)) ||
          (dp(j - 1) && s2.charAt(j - 1) == s3.charAt(i + j - 1))
      }
    }

    dp(n)
  }
}
