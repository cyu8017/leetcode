// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

object Solution {
  def isAdjacentDiffAtMostTwo(s: String): Boolean = {
    var i = 1
    while (i < s.length) {
      if (math.abs(s.charAt(i - 1) - s.charAt(i)) > 2) return false
      i += 1
    }
    true
  }
}
