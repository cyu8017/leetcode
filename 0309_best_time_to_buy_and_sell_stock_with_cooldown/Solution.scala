// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

object Solution {
  def maxProfit(prices: Array[Int]): Int = {
    if (prices.isEmpty) {
      return 0
    }
    var free = 0
    var hold = -prices(0)
    var cooldown = 0
    for (index <- 1 until prices.length) {
      val price = prices(index)
      val nextFree = math.max(free, cooldown)
      val nextHold = math.max(hold, free - price)
      val nextCooldown = hold + price
      free = nextFree
      hold = nextHold
      cooldown = nextCooldown
    }
    math.max(free, cooldown)
  }
}
