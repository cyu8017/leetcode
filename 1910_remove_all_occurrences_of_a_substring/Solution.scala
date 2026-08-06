// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

object Solution {
  def removeOccurrences(s: String, part: String): String = {
    val stack = new StringBuilder
    val m = part.length
    for (ch <- s) {
      stack.append(ch)
      if (stack.length >= m && stack.substring(stack.length - m) == part) {
        stack.delete(stack.length - m, stack.length)
      }
    }
    stack.toString
  }
}
