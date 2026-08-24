// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Long = {
    var a = if (a0 < 0) 0L else a0
    var e = e0
    var r = 1L
    a %= mod
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r
  }

  private def comb(n: Int, k: Int, mod: Int): Int = {
    if (k < 0 || k > n) return 0
    var num = 1L
    var den = 1L
    var i = 0
    while (i < k) {
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
      i += 1
    }
    (num * modPow(den, mod - 2, mod) % mod).toInt
  }

  def countGoodArrays(n: Int, m: Int, k: Int): Int = {
    val mod = 1000000007
    (comb(n - 1, k, mod).toLong * m % mod * modPow(m - 1L, n - 1L - k, mod) % mod).toInt
  }
}
