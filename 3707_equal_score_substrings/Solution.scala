// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

object Solution {
  def scoreBalance(s: String): Boolean = {
    var l = 0
    var r = 0
    for (c <- s) r += (c - 'a') + 1
    var i = 0
    while (i + 1 < s.length) {
      val x = (s.charAt(i) - 'a') + 1
      l += x
      r -= x
      if (l == r) return true
      i += 1
    }
    false
  }
}
