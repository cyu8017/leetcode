// LeetCode 0115 - Distinct Subsequences
// https://leetcode.com/problems/distinct-subsequences/

object Solution {
  def numDistinct(s: String, t: String): Int = {
    val dp = Array.fill[Long](t.length + 1)(0)
    dp(0) = 1
    for (ch <- s; j <- t.length to 1 by -1)
      if (ch == t(j - 1)) dp(j) += dp(j - 1)
    dp(t.length).toInt
  }
}