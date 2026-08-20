// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

object Solution {
  def subtractProductAndSum(n: Int): Int = {
    var product = 1
    var total = 0
    var x = n
    while (x > 0) {
      val digit = x % 10
      x /= 10
      product *= digit
      total += digit
    }
    product - total
  }
}
