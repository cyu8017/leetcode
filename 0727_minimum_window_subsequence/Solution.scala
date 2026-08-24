// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

object Solution {
  def minWindow(s1: String, s2: String): String = {
    val m = s1.length
    val n = s2.length
    var best = ""
    var i = 0
    while (i < m) {
      var j = 0
      var k = i
      while (k < m && j < n) {
        if (s1.charAt(k) == s2.charAt(j)) j += 1
        k += 1
      }
      if (j < n) return best
      val end = k - 1
      j = n - 1
      k = end
      while (j >= 0) {
        if (s1.charAt(k) == s2.charAt(j)) j -= 1
        k -= 1
      }
      val start = k + 1
      if (best.isEmpty || end - start + 1 < best.length) best = s1.substring(start, end + 1)
      i = start + 1
    }
    best
  }
}
