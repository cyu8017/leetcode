// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/

object Solution {
  private val MX = 500001
  private val MOD = 1000000007L
  private val f = new Array[Long](MX)
  private val g = new Array[Long](MX)
  private var inited = false

  private def modPow(base: Long, exp: Long): Long = {
    var a = base % MOD
    var b = exp
    var res = 1L
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res
  }

  private def ensureInit(): Unit = {
    if (inited) return
    inited = true
    f(0) = 1
    g(0) = 1
    var i = 1
    while (i < MX) {
      f(i) = f(i - 1) * i % MOD
      g(i) = modPow(f(i), MOD - 2)
      i += 1
    }
  }

  private def comb(n: Int, k: Int): Long = {
    if (k < 0 || k > n) return 0
    f(n) * g(k) % MOD * g(n - k) % MOD
  }

  def countValidSequences(n: Int, k: Int): Int = {
    ensureInit()
    var ans = comb(n - 1, k - 1)
    if ((n + k) % 2 == 0) {
      ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD
    }
    ans.toInt
  }
}
