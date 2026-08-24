// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

object Solution {
  def checkValidString(s: String): Boolean = {
    var lo = 0
    var hi = 0
    var i = 0
    while (i < s.length) {
      val ch = s.charAt(i)
      if (ch == '(') {
        lo += 1
        hi += 1
      } else if (ch == ')') {
        lo = math.max(lo - 1, 0)
        hi -= 1
        if (hi < 0) return false
      } else {
        lo = math.max(lo - 1, 0)
        hi += 1
      }
      i += 1
    }
    lo == 0
  }
}
