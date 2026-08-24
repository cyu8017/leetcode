// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

object Solution {
  def maximumSubsequenceCount(text: String, pattern: String): Long = {
    val a = pattern.charAt(0)
    val b = pattern.charAt(1)
    def count(s: String): Long = {
      var ca = 0L
      var ans = 0L
      var i = 0
      while (i < s.length) {
        val c = s.charAt(i)
        if (c == b) ans += ca
        if (c == a) ca += 1
        i += 1
      }
      ans
    }
    math.max(count(a.toString + text), count(text + b.toString))
  }
}
