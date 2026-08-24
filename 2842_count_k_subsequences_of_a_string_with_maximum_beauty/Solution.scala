// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

object Solution {
  private val MOD = 1000000007

  def countKSubsequencesWithMaxBeauty(s: String, k: Int): Int = {
    val freq = Array.fill(26)(0)
    s.foreach(c => freq(c - 'a') += 1)
    val vals = freq.filter(_ > 0).toBuffer
    if (vals.length < k) return 0
    val sorted = vals.sorted(Ordering[Int].reverse)
    val threshold = sorted(k - 1)
    var need = 0
    var avail = 0
    var prod = 1L
    sorted.foreach { v =>
      if (v > threshold) {
        prod = prod * v % MOD
        need += 1
      } else if (v == threshold) avail += 1
    }
    val remain = k - need
    prod = prod * comb(avail, remain) % MOD
    for (_ <- 0 until remain) prod = prod * threshold % MOD
    prod.toInt
  }

  private def modPow(a0: Long, b0: Long): Long = {
    var res = 1L
    var a = a0 % MOD
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res
  }

  private def comb(n: Int, r: Int): Long = {
    if (r < 0 || r > n) return 0
    var num = 1L
    var den = 1L
    for (i <- 0 until r) {
      num = num * (n - i) % MOD
      den = den * (i + 1) % MOD
    }
    num * modPow(den, MOD - 2) % MOD
  }
}
