// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

import scala.collection.mutable

object Solution {
  def minStoneSum(piles: Array[Int], k: Int): Int = {
    val heap = mutable.PriorityQueue.empty[Int]
    piles.foreach(heap.enqueue(_))
    for (_ <- 0 until k) {
      val x = heap.dequeue()
      heap.enqueue(x - x / 2)
    }
    heap.sum
  }
}
