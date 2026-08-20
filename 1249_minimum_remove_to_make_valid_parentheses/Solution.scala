// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

object Solution {
  def minRemoveToMakeValid(s: String): String = {
    val chars = s.toArray
    val opens = scala.collection.mutable.Stack[Int]()
    for (i <- chars.indices) {
      if (chars(i) == '(') opens.push(i)
      else if (chars(i) == ')') {
        if (opens.nonEmpty) opens.pop()
        else chars(i) = 0
      }
    }
    while (opens.nonEmpty) chars(opens.pop()) = 0
    chars.filter(_ != 0).mkString
  }
}
