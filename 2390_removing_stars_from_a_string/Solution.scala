// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

object Solution {
  def removeStars(s: String): String = {
    val stack = new StringBuilder
    s.foreach { c =>
      if (c == '*') stack.deleteCharAt(stack.length - 1)
      else stack.append(c)
    }
    stack.toString
  }
}
