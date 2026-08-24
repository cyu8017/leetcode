// LeetCode 3463 - Check If Digits Are Equal in String After Operations II
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

object Solution {
  private def modPowP(a0: Int, e0: Int, p: Int): Int = {
    var a = a0
    var e = e0
    var r = 1
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % p
      a = a * a % p
      e >>= 1
    }
    r
  }
  private def modInvPrime(a: Int, p: Int): Int = modPowP(a, p - 2, p)
  private def binomMod(n: Int, k: Int, p: Int): Int = {
    if (k < 0 || k > n) return 0
    var num = 1
    var den = 1
    var i = 0
    while (i < k) {
      num = num * (n - i) % p
      den = den * (i + 1) % p
      i += 1
    }
    num * modInvPrime(den, p) % p
  }
  private def crt(a1: Int, m1: Int, a2: Int, m2: Int): Int = {
    var x = 0
    while (x < m1 * m2) {
      if (x % m1 == a1 && x % m2 == a2) return x
      x += 1
    }
    0
  }
  private def binomMod10(n: Int, k: Int): Int = crt(binomMod(n, k, 2), 2, binomMod(n, k, 5), 5)
  private def combineDigit(s: String, n: Int, offset: Int): Int = {
    var sum = 0
    var i = 0
    while (i <= n - 2) {
      sum = (sum + binomMod10(n - 2, i) * (s.charAt(i + offset) - '0')) % 10
      i += 1
    }
    sum
  }
  def hasSameDigits(s: String): Boolean = {
    val n = s.length
    combineDigit(s, n, 0) == combineDigit(s, n, 1)
  }
}
