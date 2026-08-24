// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

object Solution {
  def minCost(basket1: Array[Int], basket2: Array[Int]): Long = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var mn = Int.MaxValue
    basket1.foreach { x =>
      freq(x) = freq.getOrElse(x, 0) + 1
      if (x < mn) mn = x
    }
    basket2.foreach { x =>
      freq(x) = freq.getOrElse(x, 0) - 1
      if (x < mn) mn = x
    }
    val extra = scala.collection.mutable.ArrayBuffer.empty[Int]
    freq.foreach { case (k, v) =>
      if (v % 2 != 0) return -1
      var i = 0
      while (i < math.abs(v) / 2) {
        extra += k
        i += 1
      }
    }
    val sorted = extra.sorted
    var ans = 0L
    var i = 0
    while (i < sorted.length / 2) {
      ans += math.min(sorted(i).toLong, 2L * mn)
      i += 1
    }
    ans
  }
}
