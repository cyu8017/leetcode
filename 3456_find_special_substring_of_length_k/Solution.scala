// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

object Solution {
  def hasSpecialSubstring(s: String, k: Int): Boolean = {
    val n = s.length
    var i = 0
    while (i + k <= n) {
      var ok = true
      var j = i + 1
      while (j < i + k) {
        if (s.charAt(j) != s.charAt(i)) { ok = false; j = i + k }
        else j += 1
      }
      if (ok && !(i > 0 && s.charAt(i - 1) == s.charAt(i)) && !(i + k < n && s.charAt(i + k) == s.charAt(i))) {
        return true
      }
      i += 1
    }
    false
  }
}
