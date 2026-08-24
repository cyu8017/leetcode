// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

object Solution {
  def buyChoco(prices: Array[Int], money: Int): Int = {
    scala.util.Sorting.quickSort(prices)
    val cost = prices(0) + prices(1)
    if (cost <= money) money - cost else money
  }
}
