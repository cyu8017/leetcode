// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

object Solution {
  private def qpow(a0: Long, n0: Long, mod: Long): Long = {
    var a = a0 % mod
    var n = n0
    var ans = 1L
    while (n > 0) {
      if ((n & 1) != 0) ans = ans * a % mod
      a = a * a % mod
      n >>= 1
    }
    ans
  }

  def sumOfNumbers(l: Int, r: Int, k: Int): Int = {
    val MOD = 1000000007L
    val n = r.toLong - l + 1
    val sum = (l.toLong + r) * n / 2 % MOD
    val part1 = qpow(n % MOD, k - 1, MOD)
    val part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD
    val inv9 = qpow(9, MOD - 2, MOD)
    var ans = sum
    ans = ans * part1 % MOD
    ans = ans * part2 % MOD
    ans = ans * inv9 % MOD
    ans.toInt
  }
}
