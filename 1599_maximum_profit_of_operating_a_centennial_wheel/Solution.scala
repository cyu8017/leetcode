// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

object Solution {
  def minOperationsMaxProfit(customers: Array[Int], boardingCost: Int, runningCost: Int): Int = {
    var waiting = 0
    var profit = 0
    var best = 0
    var answer = 0
    var rotation = 0
    var i = 0
    while (i < customers.length || waiting > 0) {
      if (i < customers.length) waiting += customers(i)
      val boarded = math.min(4, waiting)
      waiting -= boarded
      rotation += 1
      profit += boarded * boardingCost - runningCost
      if (profit > best) {
        best = profit
        answer = rotation
      }
      i += 1
    }
    if (best > 0) answer else -1
  }
}
