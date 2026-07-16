// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

object Solution {
  def isUgly(n: Int): Boolean = {
    var value = n
    if (value <= 0) {
      return false
    }
    for (factor <- Array(2, 3, 5)) {
      while (value % factor == 0) {
        value /= factor
      }
    }
    value == 1
  }
}
