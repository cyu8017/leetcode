// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

object Solution {
  def removeOuterParentheses(s: String): String = {
    val ans = new StringBuilder
    var depth = 0
    for (ch <- s) {
      if (ch == '(') {
        if (depth > 0) ans += ch
        depth += 1
      } else {
        depth -= 1
        if (depth > 0) ans += ch
      }
    }
    ans.toString
  }
}
