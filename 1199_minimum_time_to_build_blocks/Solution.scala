// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

object Solution {
  def minBuildTime(blocks: Array[Int], split: Int): Int = {
    val pq = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    blocks.foreach(pq.enqueue(_))
    while (pq.size > 1) {
      pq.dequeue()
      pq.enqueue(pq.dequeue() + split)
    }
    pq.dequeue()
  }
}
