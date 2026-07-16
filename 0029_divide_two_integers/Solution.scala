// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

object Solution {
  def divide(dividend: Int, divisor: Int): Int = {
    if (dividend == Int.MinValue && divisor == -1) {
      return Int.MaxValue
    }

    val negative = (dividend < 0) ^ (divisor < 0)
    var a = math.abs(dividend.toLong)
    var b = math.abs(divisor.toLong)
    var quotient = 0L

    var i = 31
    while (i >= 0) {
      if ((a >> i) >= b) {
        quotient += 1L << i
        a -= b << i
      }
      i -= 1
    }

    if (negative) -quotient.toInt else quotient.toInt
  }
}
