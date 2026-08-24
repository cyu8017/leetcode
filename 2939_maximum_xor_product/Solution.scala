// LeetCode 2939 - Maximum Xor Product
// https://leetcode.com/problems/maximum-xor-product/

object Solution {
  def maximumXorProduct(a0: Long, b0: Long, n: Int): Int = {
    val mod = 1000000007
    var a = a0
    var b = b0
    var i = n - 1
    while (i >= 0) {
      val bit = 1L << i
      val abit = a & bit
      val bbit = b & bit
      if (abit == bbit) {
        a |= bit
        b |= bit
      } else if (a > b) {
        b |= bit
        a &= ~bit
      } else {
        a |= bit
        b &= ~bit
      }
      i -= 1
    }
    ((a % mod) * (b % mod) % mod).toInt
  }
}
