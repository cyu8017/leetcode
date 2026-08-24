// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

object Solution {
  def scoreOfParentheses(s: String): Int = {
    val stack = scala.collection.mutable.ArrayDeque(0)
    s.foreach { ch =>
      if (ch == '(') stack.append(0)
      else {
        val value = stack.removeLast()
        val prev = stack.removeLast()
        stack.append(prev + math.max(2 * value, 1))
      }
    }
    stack.last
  }
}
