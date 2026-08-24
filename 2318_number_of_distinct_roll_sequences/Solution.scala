// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def distinctSequences(n: Int): Int = {
    val mod = 1000000007
    val dp = Array.ofDim[Int](n + 1, 7, 7)
    var a = 1
    while (a <= 6) {
      dp(1)(a)(0) = 1
      a += 1
    }
    var i = 2
    while (i <= n) {
      var prev = 1
      while (prev <= 6) {
        var pprev = 0
        while (pprev <= 6) {
          if (dp(i - 1)(prev)(pprev) != 0) {
            var cur = 1
            while (cur <= 6) {
              if (!(cur == prev || cur == pprev || gcd(cur, prev) != 1)) {
                dp(i)(cur)(prev) = (dp(i)(cur)(prev) + dp(i - 1)(prev)(pprev)) % mod
              }
              cur += 1
            }
          }
          pprev += 1
        }
        prev += 1
      }
      i += 1
    }
    var ans = 0
    a = 1
    while (a <= 6) {
      var b = 0
      while (b <= 6) {
        ans = (ans + dp(n)(a)(b)) % mod
        b += 1
      }
      a += 1
    }
    ans
  }
}
