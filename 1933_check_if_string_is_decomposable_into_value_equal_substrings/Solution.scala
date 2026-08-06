// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

object Solution {
  def isDecomposable(s: String): Boolean = {
    val n = s.length
    var i = 0
    var twos = 0
    while (i < n) {
      var j = i
      while (j < n && s.charAt(j) == s.charAt(i)) j += 1
      val length = j - i
      if (length % 3 == 1) return false
      if (length % 3 == 2) {
        twos += 1
        if (twos > 1) return false
      }
      i = j
    }
    twos == 1
  }
}
