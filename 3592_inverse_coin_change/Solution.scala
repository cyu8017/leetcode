// LeetCode 3592 - Inverse Coin Change
// https://leetcode.com/problems/inverse-coin-change/

object Solution {
  def findCoins(numWays: Array[Int]): Array[Int] = {
    val n = numWays.length
    val dp = new Array[Int](n + 1)
    val coins = new java.util.ArrayList[Integer]()
    dp(0) = 1
    var amt = 1
    while (amt <= n) {
      val ways = numWays(amt - 1)
      if (dp(amt) != ways) {
        if (dp(amt) + 1 == ways) {
          coins.add(amt)
          var x = amt
          while (x <= n) { dp(x) += dp(x - amt); x += 1 }
          if (dp(amt) != ways) return Array.empty[Int]
        } else return Array.empty[Int]
      }
      amt += 1
    }
    val out = new Array[Int](coins.size())
    var t = 0
    while (t < coins.size()) { out(t) = coins.get(t); t += 1 }
    out
  }
}
