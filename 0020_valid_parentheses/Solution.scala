// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

object Solution {
  def isValid(s: String): Boolean = {
    val stack = scala.collection.mutable.Stack[Char]()
    val pairs = Map(')' -> '(', ']' -> '[', '}' -> '{')

    s.foreach { ch =>
      if (ch == '(' || ch == '[' || ch == '{') {
        stack.push(ch)
      } else if (stack.isEmpty || stack.pop() != pairs(ch)) {
        return false
      }
    }

    stack.isEmpty
  }
}
