// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

object Solution {
  def backspaceCompare(s: String, t: String): Boolean = {
    def build(text: String): String = {
      val stack = new StringBuilder
      text.foreach { ch =>
        if (ch == '#') {
          if (stack.nonEmpty) stack.deleteCharAt(stack.length - 1)
        } else stack.append(ch)
      }
      stack.toString
    }
    build(s) == build(t)
  }
}
