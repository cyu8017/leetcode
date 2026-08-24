// LeetCode 2233 - Maximum Product After K Increments
// https://leetcode.com/problems/maximum-product-after-k-increments/

object Solution {
  def maximumProduct(nums: Array[Int], k: Int): Int = {
    val MOD = 1000000007
    val h = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    for (x <- nums) h.enqueue(x)
    var i = 0
    while (i < k) {
      val x = h.dequeue()
      h.enqueue(x + 1)
      i += 1
    }
    var ans = 1L
    while (h.nonEmpty) ans = ans * h.dequeue() % MOD
    ans.toInt
  }
}
