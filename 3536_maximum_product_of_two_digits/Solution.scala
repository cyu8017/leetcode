// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

object Solution {
  def maxProduct(n0: Int): Int = {
    var n = n0
    var a = 0
    var b = 0
    while (n > 0) {
      val x = n % 10
      if (a < x) { b = a; a = x }
      else if (b < x) b = x
      n /= 10
    }
    a * b
  }
}
