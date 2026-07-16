// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

def isBadVersion(version: Int): Boolean = false

object Solution {
  def firstBadVersion(n: Int): Int = {
    var left = 1
    var right = n
    while (left < right) {
      val mid = left + (right - left) / 2
      if (isBadVersion(mid)) {
        right = mid
      } else {
        left = mid + 1
      }
    }
    left
  }
}
