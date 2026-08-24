// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

object Solution {
  def numberOfWays(startPos: Int, endPos: Int, k: Int): Int = {
    val mod = 1000000007
    val diff = math.abs(endPos - startPos)
    if (diff > k || (k - diff) % 2 != 0) return 0
    val r = (k + diff) / 2
    comb(k, r, mod)
  }

  private def comb(n: Int, r: Int, mod: Int): Int = {
    if (r < 0 || r > n) return 0
    var num = 1L
    var den = 1L
    var i = 0
    while (i < r) {
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
      i += 1
    }
    (num * modInverse(den.toInt, mod) % mod).toInt
  }

  private def modInverse(a: Int, mod: Int): Int = modPow(a, mod - 2, mod)

  private def modPow(a: Int, e0: Int, mod: Int): Int = {
    var res = 1L
    var base = a % mod
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) res = res * base % mod
      base = base * base % mod
      e >>= 1
    }
    res.toInt
  }
}
