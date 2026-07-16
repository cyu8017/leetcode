// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

object Solution {
  def repeatedSubstringPattern(s: String): Boolean = {
    val doubled = s + s
    doubled.substring(1, doubled.length - 1).contains(s)
  }
}
