// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

object Solution {
  def maxIceCream(costs: Array[Int], coins: Int): Int = {
    val sorted = costs.sorted
    var remaining = coins
    var count = 0
    for (cost <- sorted) {
      if (remaining < cost) return count
      remaining -= cost
      count += 1
    }
    count
  }
}
