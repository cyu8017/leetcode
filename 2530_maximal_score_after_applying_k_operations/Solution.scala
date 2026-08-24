// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

object Solution {
  def maxKelements(nums: Array[Int], k: Int): Long = {
    val pq = scala.collection.mutable.PriorityQueue.empty[Int]
    nums.foreach(x => pq.enqueue(x))
    var ans = 0L
    var i = 0
    while (i < k) {
      val x = pq.dequeue()
      ans += x
      pq.enqueue((x + 2) / 3)
      i += 1
    }
    ans
  }
}
