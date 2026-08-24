// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

object Solution {
  def hasMatch(s: String, p: String): Boolean = {
    val i = p.indexOf('*')
    val left = p.substring(0, i)
    val right = p.substring(i + 1)
    val li = s.indexOf(left)
    if (li < 0) return false
    s.indexOf(right, li + left.length) >= 0
  }
}
