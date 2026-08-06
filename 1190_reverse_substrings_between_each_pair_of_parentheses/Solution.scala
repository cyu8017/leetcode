// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

object Solution {
  def reverseParentheses(s: String): String = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Char]
    for (ch <- s) {
      if (ch == ')') {
        val chunk = scala.collection.mutable.ArrayBuffer.empty[Char]
        while (stack.nonEmpty && stack.last != '(') chunk += stack.remove(stack.length - 1)
        stack.remove(stack.length - 1)
        stack ++= chunk
      } else stack += ch
    }
    stack.mkString
  }
}
