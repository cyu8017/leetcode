// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

object Solution {
  def minNonZeroProduct(p: Int): Int = {
    val MOD = 1000000007L
    def modPow(base: Long, exp: Long): Long = {
      var b = base % MOD
      var e = exp
      var res = 1L
      while (e > 0) {
        if ((e & 1) == 1) res = res * b % MOD
        b = b * b % MOD
        e >>= 1
      }
      res
    }
    val mx = (1L << p) - 1
    ((mx % MOD) * modPow(mx - 1, (1L << (p - 1)) - 1) % MOD).toInt
  }
}
