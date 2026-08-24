// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

object Solution {
  def maximumAmount(coins: Array[Array[Int]]): Int = {
    val m = coins.length
    val n = coins(0).length
    val neg = -(1 << 30)
    val dp = Array.fill(m, n, 3)(neg)
    if (coins(0)(0) < 0) {
      dp(0)(0)(0) = coins(0)(0)
      dp(0)(0)(1) = 0
      dp(0)(0)(2) = 0
    } else {
      dp(0)(0)(0) = coins(0)(0)
      dp(0)(0)(1) = coins(0)(0)
      dp(0)(0)(2) = coins(0)(0)
    }
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (!(i == 0 && j == 0)) {
          var k = 0
          while (k < 3) {
            var best = neg
            if (i > 0) best = math.max(best, dp(i - 1)(j)(k))
            if (j > 0) best = math.max(best, dp(i)(j - 1)(k))
            if (best != neg) {
              if (coins(i)(j) >= 0) dp(i)(j)(k) = best + coins(i)(j)
              else dp(i)(j)(k) = math.max(dp(i)(j)(k), best + coins(i)(j))
            }
            k += 1
          }
          k = 1
          while (k < 3) {
            var best = neg
            if (i > 0) best = math.max(best, dp(i - 1)(j)(k - 1))
            if (j > 0) best = math.max(best, dp(i)(j - 1)(k - 1))
            if (best != neg && coins(i)(j) < 0) dp(i)(j)(k) = math.max(dp(i)(j)(k), best)
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    math.max(dp(m - 1)(n - 1)(0), math.max(dp(m - 1)(n - 1)(1), dp(m - 1)(n - 1)(2)))
  }
}
