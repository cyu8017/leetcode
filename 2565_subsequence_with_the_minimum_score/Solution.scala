// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

object Solution {
  def minimumScore(s: String, t: String): Int = {
    val n = s.length
    val m = t.length
    val left = Array.fill(m)(-1)
    val right = Array.fill(m)(-1)
    var j = 0
    var i = 0
    while (i < n && j < m) {
      if (s.charAt(i) == t.charAt(j)) {
        left(j) = i
        j += 1
      }
      i += 1
    }
    j = m - 1
    i = n - 1
    while (i >= 0 && j >= 0) {
      if (s.charAt(i) == t.charAt(j)) {
        right(j) = i
        j -= 1
      }
      i -= 1
    }
    if (left(m - 1) != -1) return 0
    var ans = m
    i = 0
    var found = false
    while (i < m && !found) {
      if (right(i) != -1) {
        if (i < ans) ans = i
        found = true
      }
      i += 1
    }
    i = m - 1
    found = false
    while (i >= 0 && !found) {
      if (left(i) != -1) {
        if (m - 1 - i < ans) ans = m - 1 - i
        found = true
      }
      i -= 1
    }
    j = 0
    i = 0
    while (i < m) {
      if (left(i) == -1) return ans
      while (j < m && (right(j) == -1 || right(j) <= left(i))) j += 1
      if (j < m) {
        val rem = j - i - 1
        if (rem < ans) ans = rem
      }
      i += 1
    }
    ans
  }
}
