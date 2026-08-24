// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

object Solution {
  def mostFrequentIDs(nums: Array[Int], freq: Array[Int]): Array[Long] = {
    val n = nums.length
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val lazyMap = scala.collection.mutable.Map.empty[Int, Int]
    val ans = new Array[Long](n)
    val pq = new java.util.PriorityQueue[Integer]((a: Integer, b: Integer) => b - a)
    var i = 0
    while (i < n) {
      val x = nums(i)
      val f = freq(i)
      val old = cnt.getOrElse(x, 0)
      lazyMap(old) = lazyMap.getOrElse(old, 0) + 1
      val neu = old + f
      cnt(x) = neu
      pq.offer(neu)
      while (!pq.isEmpty && lazyMap.getOrElse(pq.peek(), 0) > 0) {
        val top = pq.poll()
        lazyMap(top) = lazyMap(top) - 1
      }
      if (!pq.isEmpty) ans(i) = pq.peek().toLong
      i += 1
    }
    ans
  }
}
