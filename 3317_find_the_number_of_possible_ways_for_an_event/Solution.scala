// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

object Solution {
  private def modPow(a0: Long, e0: Long, mod: Int): Int = {
    var r = 1L
    var a = a0 % mod
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) r = r * a % mod
      a = a * a % mod
      e >>= 1
    }
    r.toInt
  }

  def numberOfWays(n: Int, x: Int, y: Int): Int = {
    val mod = 1000000007
    val dp = Array.ofDim[Int](n + 1, x + 1)
    dp(0)(0) = 1
    var i = 1
    while (i <= n) {
      var j = 1
      while (j <= x && j <= i) {
        dp(i)(j) = (dp(i - 1)(j - 1) + (j.toLong * dp(i - 1)(j) % mod).toInt) % mod
        j += 1
      }
      i += 1
    }
    val fact = new Array[Int](x + 1)
    fact(0) = 1
    i = 1
    while (i <= x) {
      fact(i) = (fact(i - 1).toLong * i % mod).toInt
      i += 1
    }
    var ans = 0
    var ypow = 1
    var k = 1
    while (k <= x && k <= n) {
      ypow = (ypow.toLong * y % mod).toInt
      val perm = (fact(x).toLong * modPow(fact(x - k).toLong, mod - 2, mod) % mod).toInt
      ans = (ans + (dp(n)(k).toLong * perm % mod * ypow % mod).toInt) % mod
      k += 1
    }
    ans
  }
}
