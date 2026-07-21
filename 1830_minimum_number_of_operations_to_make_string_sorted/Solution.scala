// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

object Solution {
  def makeStringSorted(s: String): Int = {
    val MOD = 1000000007L
    val n = s.length
    val fact = Array.fill(n + 1)(1L)
    for (i <- 2 to n) fact(i) = fact(i - 1) * i % MOD
    val invFact = Array.fill(n + 1)(1L)
    invFact(n) = modPow(fact(n), MOD - 2, MOD)
    for (i <- n - 1 to 0 by -1) invFact(i) = invFact(i + 1) * (i + 1) % MOD

    val freq = Array.fill(26)(0)
    for (ch <- s) freq(ch - 'a') += 1

    var ans = 0L
    for (i <- 0 until n) {
      val c = s(i) - 'a'
      for (smaller <- 0 until c if freq(smaller) > 0) {
        freq(smaller) -= 1
        var ways = fact(n - i - 1)
        for (count <- freq) ways = ways * invFact(count) % MOD
        ans = (ans + ways) % MOD
        freq(smaller) += 1
      }
      freq(c) -= 1
    }
    ans.toInt
  }

  private def modPow(base: Long, exp: Long, mod: Long): Long = {
    var b = base % mod
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1) == 1) res = res * b % mod
      b = b * b % mod
      e >>= 1
    }
    res
  }
}
