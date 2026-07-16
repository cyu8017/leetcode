// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

object Solution {
  def isNumber(s: String): Boolean = {
    var seenDigit = false
    var seenDot = false
    var seenExp = false

    var i = 0
    while (i < s.length) {
      val ch = s(i)
      if (ch.isDigit) {
        seenDigit = true
      } else if (ch == '+' || ch == '-') {
        if (i > 0 && s(i - 1) != 'e' && s(i - 1) != 'E') {
          return false
        }
      } else if (ch == 'e' || ch == 'E') {
        if (seenExp || !seenDigit) {
          return false
        }
        seenExp = true
        seenDigit = false
        seenDot = false
      } else if (ch == '.') {
        if (seenDot || seenExp) {
          return false
        }
        seenDot = true
      } else {
        return false
      }
      i += 1
    }

    seenDigit
  }
}
