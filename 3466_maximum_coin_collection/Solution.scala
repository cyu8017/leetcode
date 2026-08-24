// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

object Solution {
  def maxCoins(lane1: Array[Int], lane2: Array[Int]): Long = {
    val n = lane1.length
    val neg = -1L << 60
    val dp = Array.ofDim[Long](2, 2)
    dp(0)(0) = lane1(0)
    dp(1)(0) = lane2(0)
    dp(0)(1) = neg
    dp(1)(1) = neg
    var ans = math.max(dp(0)(0), dp(1)(0))
    var i = 1
    while (i < n) {
      val ndp = Array.ofDim[Long](2, 2)
      ndp(0)(0) = math.max(dp(0)(0), 0L) + lane1(i)
      ndp(1)(0) = math.max(dp(1)(0), 0L) + lane2(i)
      ndp(0)(1) = math.max(dp(0)(1), dp(1)(0)) + lane1(i)
      ndp(1)(1) = math.max(dp(1)(1), dp(0)(0)) + lane2(i)
      if (lane1(i) > ndp(0)(0)) ndp(0)(0) = lane1(i)
      if (lane2(i) > ndp(1)(0)) ndp(1)(0) = lane2(i)
      var a = 0
      while (a < 2) {
        var b = 0
        while (b < 2) {
          dp(a)(b) = ndp(a)(b)
          if (dp(a)(b) > ans) ans = dp(a)(b)
          b += 1
        }
        a += 1
      }
      i += 1
    }
    ans
  }
}
