// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

import scala.collection.mutable

object Solution {
  def maxItems(items: Array[Array[Int]], budget: Int): Int = {
    val n = items.length
    val frequency = new Array[Int](n + 1)
    var minimumPrice = items(0)(1)
    for (item <- items) {
      frequency(item(0)) += 1
      minimumPrice = math.min(minimumPrice, item(1))
    }
    val batches = mutable.ArrayBuffer.empty[(Int, Int)]
    for (item <- items) {
      var gain = 0
      var multiple = item(0)
      while (multiple <= n) {
        gain += frequency(multiple)
        multiple += item(0)
      }
      gain -= 1
      if (gain > 0 && item(1) < 2 * minimumPrice) batches += ((item(1), gain))
    }
    val sorted = batches.sortBy(_._1)
    var remaining = budget.toLong
    var answer = budget.toLong / minimumPrice
    var boosted = 0L
    var broken = false
    for (current <- sorted if !broken) {
      var count = current._2.toLong
      val affordable = remaining / current._1
      if (affordable < count) count = affordable
      remaining -= count * current._1
      boosted += count
      val total = 2 * boosted + remaining / minimumPrice
      if (total > answer) answer = total
      if (count < current._2) broken = true
    }
    answer.toInt
  }
}
