// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
// https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import scala.collection.mutable

object Solution {
  def smallestChair(times: Array[Array[Int]], targetFriend: Int): Int = {
    val order = times.indices.sortBy(i => times(i)(0))
    val free = mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    var nextChair = 0
    val leaving = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](-_._1))
    for (i <- order) {
      val arr = times(i)(0)
      val leave = times(i)(1)
      while (leaving.nonEmpty && leaving.head._1 <= arr) {
        free.enqueue(leaving.dequeue()._2)
      }
      val chair = if (free.nonEmpty) free.dequeue() else { val c = nextChair; nextChair += 1; c }
      if (i == targetFriend) return chair
      leaving.enqueue((leave, chair))
    }
    -1
  }
}
