// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

object Solution {
  def maximizeTheProfit(n: Int, offers: List[List[Int]]): Int = {
    val byEnd = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[List[Int]])
    offers.foreach { o =>
      byEnd(o(1)) += o
    }
    val dp = Array.ofDim[Int](n + 1)
    var end = 0
    while (end < n) {
      dp(end + 1) = dp(end)
      byEnd(end).foreach { o =>
        dp(end + 1) = math.max(dp(end + 1), dp(o.head) + o(2))
      }
      end += 1
    }
    dp(n)
  }
}
