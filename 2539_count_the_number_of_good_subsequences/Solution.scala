// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

object Solution {
  private val MOD = 1000000007

  private def modPow(a0: Long, e0: Long): Long = {
    var res = 1L
    var a = a0
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      e >>= 1
    }
    res
  }

  def countGoodSubsequences(s: String): Int = {
    val cnt = Array.fill(26)(0)
    var maxf = 0
    s.foreach { c =>
      cnt(c - 'a') += 1
      if (cnt(c - 'a') > maxf) maxf = cnt(c - 'a')
    }
    val fact = Array.fill(maxf + 1)(0L)
    val invFact = Array.fill(maxf + 1)(0L)
    fact(0) = 1
    var i = 1
    while (i <= maxf) {
      fact(i) = fact(i - 1) * i % MOD
      i += 1
    }
    invFact(maxf) = modPow(fact(maxf), MOD - 2)
    i = maxf
    while (i > 0) {
      invFact(i - 1) = invFact(i) * i % MOD
      i -= 1
    }
    def comb(n: Int, k: Int): Long = {
      if (k < 0 || k > n) 0L
      else fact(n) * invFact(k) % MOD * invFact(n - k) % MOD
    }
    var ans = 0L
    var k = 1
    while (k <= maxf) {
      var ways = 1L
      i = 0
      while (i < 26) {
        if (cnt(i) >= k) ways = ways * (1 + comb(cnt(i), k)) % MOD
        i += 1
      }
      ans = (ans + ways - 1 + MOD) % MOD
      k += 1
    }
    ans.toInt
  }
}
