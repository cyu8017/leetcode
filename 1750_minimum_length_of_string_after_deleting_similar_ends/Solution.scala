// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

object Solution {
  def minimumLength(s: String): Int = {
    var left = 0
    var right = s.length - 1
    while (left < right && s(left) == s(right)) {
      val ch = s(left)
      while (left <= right && s(left) == ch) {
        left += 1
      }
      while (left <= right && s(right) == ch) {
        right -= 1
      }
    }
    right - left + 1
  }
}
