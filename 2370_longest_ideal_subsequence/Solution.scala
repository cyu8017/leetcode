// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

object Solution {
  def longestIdealString(s: String, k: Int): Int = {
    val dp = Array.fill(26)(0)
    var ans = 0
    s.foreach { ch =>
      val c = ch - 'a'
      var best = 0
      var p = 0
      while (p < 26) {
        if (math.abs(c - p) <= k && dp(p) > best) best = dp(p)
        p += 1
      }
      dp(c) = best + 1
      ans = math.max(ans, dp(c))
    }
    ans
  }
}
