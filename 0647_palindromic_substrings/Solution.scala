// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

object Solution {
  def countSubstrings(s: String): Int = {
    var total = 0
    var i = 0
    while (i < s.length) {
      total += expand(s, i, i)
      total += expand(s, i, i + 1)
      i += 1
    }
    total
  }

  private def expand(s: String, left0: Int, right0: Int): Int = {
    var left = left0
    var right = right0
    var count = 0
    while (left >= 0 && right < s.length && s.charAt(left) == s.charAt(right)) {
      count += 1
      left -= 1
      right += 1
    }
    count
  }
}
