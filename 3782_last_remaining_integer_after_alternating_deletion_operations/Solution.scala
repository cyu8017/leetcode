// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

object Solution {
  def lastRemaining(n0: Long): Long = {
    var n = n0
    var first = 1L
    var step = 2L
    var left = true
    while (n > 1) {
      if (!left && n % 2 == 0) first += step
      n = (n + 1) / 2
      step *= 2
      left = !left
    }
    first
  }
}
