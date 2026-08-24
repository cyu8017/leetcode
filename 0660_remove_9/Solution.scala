// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

object Solution {
  def newInteger(n0: Int): Int = {
    var n = n0
    var result = 0
    var base = 1
    while (n > 0) {
      result += (n % 9) * base
      n /= 9
      base *= 10
    }
    result
  }
}
