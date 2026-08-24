// LeetCode 2280 - Minimum Lines to Represent a Line Chart
// https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

object Solution {
  def minimumLines(stockPrices: Array[Array[Int]]): Int = {
    if (stockPrices.length <= 1) return 0
    java.util.Arrays.sort(stockPrices, (a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    var ans = 1
    var i = 2
    while (i < stockPrices.length) {
      val x0 = stockPrices(i - 2)(0).toLong
      val y0 = stockPrices(i - 2)(1).toLong
      val x1 = stockPrices(i - 1)(0).toLong
      val y1 = stockPrices(i - 1)(1).toLong
      val x2 = stockPrices(i)(0).toLong
      val y2 = stockPrices(i)(1).toLong
      if ((y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0)) ans += 1
      i += 1
    }
    ans
  }
}
