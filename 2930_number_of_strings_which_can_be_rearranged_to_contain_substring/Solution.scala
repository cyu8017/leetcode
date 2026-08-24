// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

object Solution {
  private val MOD = 1000000007

  def stringCount(n: Int): Int = {
    if (n < 4) return 0
    var ans = modPow(26, n).toLong
    ans = (ans - 3L * modPow(25, n) % MOD + MOD) % MOD
    ans = (ans + 3L * modPow(24, n) % MOD) % MOD
    ans = (ans - modPow(23, n) + MOD) % MOD
    ans = (ans + 1L * (n % MOD) * modPow(25, n - 1) % MOD) % MOD
    ans = (ans - 2L * (n % MOD) % MOD * modPow(24, n - 1) % MOD + MOD) % MOD
    ans = (ans + 1L * (n % MOD) * modPow(23, n - 1) % MOD) % MOD
    ans = (ans - 1L * (n % MOD) * ((n - 1 + MOD) % MOD) % MOD * modPow(24, n - 2) % MOD % MOD + MOD) % MOD
    ans = (ans + 1L * (n % MOD) * ((n - 1 + MOD) % MOD) % MOD * modPow(23, n - 2) % MOD) % MOD
    ans.toInt
  }

  private def modPow(a0: Long, b0: Int): Int = {
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
