// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

import scala.collection.mutable

object Solution {
  def smallestFactorization(num0: Int): Int = {
    var num = num0
    if (num < 10) return num
    val digits = mutable.ArrayBuffer.empty[Int]
    var digit = 9
    while (digit >= 2) {
      while (num % digit == 0) {
        digits += digit
        num /= digit
      }
      digit -= 1
    }
    if (num != 1) return 0
    var result = 0L
    var i = digits.size - 1
    while (i >= 0) {
      result = result * 10 + digits(i)
      if (result > Int.MaxValue) return 0
      i -= 1
    }
    result.toInt
  }
}
