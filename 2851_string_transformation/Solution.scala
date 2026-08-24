// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

object Solution {
  private val MOD = 1000000007

  def numberOfWays(s: String, t: String, k: Long): Int = {
    val n = s.length
    val ss = s + s
    if (!ss.substring(0, 2 * n - 1).contains(t)) return 0
    var cnt = 0
    for (i <- 0 until n) if (ss.substring(i, i + n) == t) cnt += 1
    val same = s == t
    val pk = modPow(n - 1, k)
    val invn = modPow(n, MOD - 2)
    val sign = if (k % 2 == 1) MOD - 1 else 1
    val waysSame = ((1L * pk + 1L * ((n - 1) % MOD) * sign % MOD) % MOD * invn % MOD).toInt
    val waysDiff = ((1L * pk - sign + MOD) % MOD * invn % MOD).toInt
    if (same) waysSame else (1L * waysDiff * cnt % MOD).toInt
  }

  private def modPow(a0: Long, b0: Long): Int = {
    var res = 1L
    var a = a0 % MOD
    var b = b0
    while (b > 0) {
      if ((b & 1) != 0) res = res * a % MOD
      a = a * a % MOD
      b >>= 1
    }
    res.toInt
  }
}
