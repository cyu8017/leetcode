// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

object Solution {
  def numberOfWays(n: Int, x: Int): Int = {
    val MOD = 1000000007
    val powers = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    var stop = false
    while (!stop) {
      var p = 1L
      var j = 0
      var over = false
      while (j < x && !over) {
        p *= i
        if (p > n) over = true
        j += 1
      }
      if (p > n) stop = true
      else {
        powers += p.toInt
        i += 1
      }
    }
    val dp = Array.ofDim[Int](n + 1)
    dp(0) = 1
    powers.foreach { p =>
      var s = n
      while (s >= p) {
        dp(s) = (dp(s) + dp(s - p)) % MOD
        s -= 1
      }
    }
    dp(n)
  }
}
