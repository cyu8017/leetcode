// LeetCode 2430 - Maximum Deletions on a String
// https://leetcode.com/problems/maximum-deletions-on-a-string/

object Solution {
  def deleteString(s: String): Int = {
    val n = s.length
    val lcp = Array.ofDim[Int](n + 1, n + 1)
    var i = n - 1
    while (i >= 0) {
      var j = n - 1
      while (j >= 0) {
        if (s.charAt(i) == s.charAt(j)) lcp(i)(j) = lcp(i + 1)(j + 1) + 1
        j -= 1
      }
      i -= 1
    }
    val dp = new Array[Int](n)
    i = n - 1
    while (i >= 0) {
      dp(i) = 1
      var len = 1
      while (i + 2 * len <= n) {
        if (lcp(i)(i + len) >= len) {
          val v = 1 + dp(i + len)
          if (v > dp(i)) dp(i) = v
        }
        len += 1
      }
      i -= 1
    }
    dp(0)
  }
}
