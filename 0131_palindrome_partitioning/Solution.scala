// LeetCode 0131 - Palindrome Partitioning
// https://leetcode.com/problems/palindrome-partitioning/

import scala.collection.mutable.ListBuffer

object Solution {
  def partition(s: String): List[List[String]] = {
    val result = ListBuffer[List[String]]()
    def isPalindrome(leftStart: Int, rightStart: Int): Boolean = {
      var left = leftStart
      var right = rightStart
      while (left < right) {
        if (s(left) != s(right)) return false
        left += 1
        right -= 1
      }
      true
    }
    def dfs(start: Int, path: List[String]): Unit = {
      if (start == s.length) result += path
      else for (end <- start until s.length if isPalindrome(start, end)) dfs(end + 1, path :+ s.substring(start, end + 1))
    }
    dfs(0, Nil)
    result.toList
  }
}
