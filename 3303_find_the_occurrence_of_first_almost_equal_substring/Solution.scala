// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

object Solution {
  def minStartingIndex(s: String, pattern: String): Int = {
    val n = s.length
    val m = pattern.length
    var i = 0
    while (i + m <= n) {
      var diff = 0
      var j = 0
      while (j < m) {
        if (s.charAt(i + j) != pattern.charAt(j)) {
          diff += 1
          if (diff > 1) j = m
        }
        if (j < m) j += 1
      }
      if (diff <= 1) return i
      i += 1
    }
    -1
  }
}
