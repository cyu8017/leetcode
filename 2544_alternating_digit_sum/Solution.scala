// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

object Solution {
  def alternateDigitSum(n: Int): Int = {
    val digits = Array.fill(12)(0)
    var len = 0
    var x = n
    while (x > 0) {
      digits(len) = x % 10
      len += 1
      x /= 10
    }
    var ans = 0
    var sign = 1
    var i = len - 1
    while (i >= 0) {
      ans += sign * digits(i)
      sign = -sign
      i -= 1
    }
    ans
  }
}
