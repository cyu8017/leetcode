// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

import scala.collection.mutable

object Solution {
  def lastStoneWeight(stones: Array[Int]): Int = {
    val pq = mutable.PriorityQueue[Int](stones: _*)
    while (pq.size > 1) {
      val a = pq.dequeue()
      val b = pq.dequeue()
      if (a != b) pq.enqueue(a - b)
    }
    if (pq.isEmpty) 0 else pq.dequeue()
  }
}
