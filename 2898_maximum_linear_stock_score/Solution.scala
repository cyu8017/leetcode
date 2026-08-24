// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

object Solution {
  def maxScore(prices: Array[Int]): Long = {
    val best = scala.collection.mutable.Map.empty[Int, Long]
    var ans = 0L
    for (i <- prices.indices) {
      val key = prices(i) - (i + 1)
      val cand = best.getOrElse(key, 0L) + prices(i)
      if (cand > best.getOrElse(key, 0L)) best(key) = cand
      if (best(key) > ans) ans = best(key)
    }
    ans
  }
}
