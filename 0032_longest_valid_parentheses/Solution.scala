// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

object Solution {
  def longestValidParentheses(s: String): Int = {
    val stack = scala.collection.mutable.ArrayStack.empty[Int]
    stack.push(-1)
    var best = 0

    s.indices.foreach { i =>
      if (s(i) == '(') {
        stack.push(i)
      } else {
        stack.pop()
        if (stack.isEmpty) {
          stack.push(i)
        } else {
          best = math.max(best, i - stack.top)
        }
      }
    }

    best
  }
}
