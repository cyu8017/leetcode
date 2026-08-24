// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

object Solution {
  def beautifulPartitions(s: String, k: Int, minLength: Int): Int = {
    def isPrime(c: Char): Boolean = c == '2' || c == '3' || c == '5' || c == '7'
    val mod = 1000000007
    val n = s.length
    if (!isPrime(s.charAt(0)) || isPrime(s.charAt(n - 1))) return 0
    val dp = Array.ofDim[Int](k + 1, n + 1)
    dp(0)(0) = 1
    var p = 1
    while (p <= k) {
      var pref = 0
      var j = 0
      var i = 1
      while (i <= n) {
        while (j <= i - minLength) {
          if (j == 0 || (isPrime(s.charAt(j)) && !isPrime(s.charAt(j - 1)))) {
            pref = (pref + dp(p - 1)(j)) % mod
          }
          j += 1
        }
        if (!isPrime(s.charAt(i - 1))) dp(p)(i) = pref
        i += 1
      }
      p += 1
    }
    dp(k)(n)
  }
}
