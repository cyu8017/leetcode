// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

object Solution {
  def maxProfit(prices: Array[Int]): Int = {
    var buy1 = Int.MaxValue
    var buy2 = Int.MaxValue
    var sell1 = 0
    var sell2 = 0
    for (price <- prices) {
      buy1 = Math.min(buy1, price)
      sell1 = Math.max(sell1, price - buy1)
      buy2 = Math.min(buy2, price - sell1)
      sell2 = Math.max(sell2, price - buy2)
    }
    sell2
  }
}