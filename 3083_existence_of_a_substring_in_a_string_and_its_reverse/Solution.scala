// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

object Solution {
  def isSubstringPresent(s: String): Boolean = {
    val st = Array.ofDim[Boolean](26, 26)
    var i = 0
    while (i + 1 < s.length) {
      st(s.charAt(i + 1) - 'a')(s.charAt(i) - 'a') = true
      i += 1
    }
    i = 0
    while (i + 1 < s.length) {
      if (st(s.charAt(i) - 'a')(s.charAt(i + 1) - 'a')) return true
      i += 1
    }
    false
  }
}
