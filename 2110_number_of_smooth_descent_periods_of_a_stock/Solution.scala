// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

object Solution {
  def getDescentPeriods(prices: Array[Int]): Long = {
    var ans = 1L
    var cur = 1L
    var i = 1
    while (i < prices.length) {
      if (prices(i) == prices(i - 1) - 1) cur += 1
      else cur = 1
      ans += cur
      i += 1
    }
    ans
  }
}
