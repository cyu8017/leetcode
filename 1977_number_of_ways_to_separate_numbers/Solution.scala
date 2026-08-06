// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

object Solution {
  def numberOfCombinations(num: String): Int = {
    val MOD = 1000000007
    val n = num.length
    if (num.charAt(0) == '0') return 0

    val lcp = Array.ofDim[Int](n + 1, n + 1)
    for (i <- n - 1 to 0 by -1; j <- n - 1 to 0 by -1) {
      if (num.charAt(i) == num.charAt(j)) lcp(i)(j) = lcp(i + 1)(j + 1) + 1
    }

    def le(a: Int, b: Int, length: Int): Boolean = {
      val common = lcp(a)(b)
      if (common >= length) true
      else num.charAt(a + common) < num.charAt(b + common)
    }

    val dp = Array.ofDim[Int](n + 1, n + 1)
    val pref = Array.ofDim[Int](n + 1, n + 1)
    for (i <- 1 to n) {
      for (l <- 1 to i) {
        val start = i - l
        if (num.charAt(start) == '0') dp(i)(l) = 0
        else if (start == 0) dp(i)(l) = 1
        else {
          var ways = if (l > 1) pref(start)(math.min(l - 1, start)) else 0
          if (start >= l && le(start - l, start, l)) ways = (ways + dp(start)(l)) % MOD
          dp(i)(l) = ways
        }
      }
      for (l <- 1 to n) {
        pref(i)(l) = (pref(i)(l - 1) + (if (l <= i) dp(i)(l) else 0)) % MOD
      }
    }
    pref(n)(n)
  }
}
