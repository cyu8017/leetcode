// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

object Solution {
  def removeZeros(n0: Long): Long = {
    var n = n0
    var ans = 0L
    var k = 1L
    while (n > 0) {
      val x = n % 10
      if (x > 0) {
        ans = k * x + ans
        k *= 10
      }
      n /= 10
    }
    ans
  }
}
