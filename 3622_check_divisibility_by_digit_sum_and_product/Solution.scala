// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

object Solution {
  def checkDivisibility(n: Int): Boolean = {
    var s = 0
    var p = 1
    var x = n
    while (x != 0) {
      val v = x % 10
      x /= 10
      s += v
      p *= v
    }
    n % (s + p) == 0
  }
}
