// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

object Solution {
  def rotateString(s: String, goal: String): Boolean = {
    s.length == goal.length && (s + s).contains(goal)
  }
}
