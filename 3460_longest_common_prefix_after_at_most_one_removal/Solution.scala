// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

object Solution {
  def longestCommonPrefix(s: String, t: String): Int = {
    var i = 0
    var j = 0
    var removed = false
    while (i < s.length && j < t.length) {
      if (s.charAt(i) == t.charAt(j)) {
        i += 1
        j += 1
      } else {
        if (removed) return j
        removed = true
        i += 1
      }
    }
    j
  }
}
