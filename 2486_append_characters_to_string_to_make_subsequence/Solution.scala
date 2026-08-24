// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

object Solution {
  def appendCharacters(s: String, t: String): Int = {
    var j = 0
    var i = 0
    while (i < s.length && j < t.length) {
      if (s.charAt(i) == t.charAt(j)) j += 1
      i += 1
    }
    t.length - j
  }
}
