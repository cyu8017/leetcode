// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

object Solution {
  def canBeValid(s: String, locked: String): Boolean = {
    val n = s.length
    if (n % 2 != 0) return false
    var bal = 0
    var i = 0
    while (i < n) {
      if (locked.charAt(i) == '0' || s.charAt(i) == '(') bal += 1
      else bal -= 1
      if (bal < 0) return false
      i += 1
    }
    bal = 0
    i = n - 1
    while (i >= 0) {
      if (locked.charAt(i) == '0' || s.charAt(i) == ')') bal += 1
      else bal -= 1
      if (bal < 0) return false
      i -= 1
    }
    true
  }
}
