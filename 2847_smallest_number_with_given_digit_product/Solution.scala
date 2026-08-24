// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

object Solution {
  def smallestNumber(n: Long): String = {
    if (n == 0) return "0"
    if (n == 1) return "1"
    val digits = new StringBuilder
    var x = n
    for (d <- 9 to 2 by -1) {
      while (x % d == 0) {
        digits.append(('0' + d).toChar)
        x /= d
      }
    }
    if (x > 1) "-1" else digits.reverse.toString
  }
}
