// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

object Solution {
  def countGoodNumbers(n: Long): Int = {
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
    (modPow(5, (n + 1) / 2) * modPow(4, n / 2) % MOD).toInt
  }
}
