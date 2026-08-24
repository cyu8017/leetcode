// LeetCode 2337 - Move Pieces to Obtain a String
// https://leetcode.com/problems/move-pieces-to-obtain-a-string/

object Solution {
  def canChange(start: String, target: String): Boolean = {
    val n = start.length
    var i = 0
    var j = 0
    while (i < n || j < n) {
      while (i < n && start.charAt(i) == '_') i += 1
      while (j < n && target.charAt(j) == '_') j += 1
      if (i == n || j == n) return i == n && j == n
      if (start.charAt(i) != target.charAt(j)) return false
      if (start.charAt(i) == 'L' && i < j) return false
      if (start.charAt(i) == 'R' && i > j) return false
      i += 1
      j += 1
    }
    true
  }
}
