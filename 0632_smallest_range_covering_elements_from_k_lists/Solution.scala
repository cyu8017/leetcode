// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import scala.collection.mutable

object Solution {
  def smallestRange(nums: List[List[Int]]): Array[Int] = {
    implicit val ord: Ordering[Array[Int]] = Ordering.by((a: Array[Int]) => -a(0))
    val heap = mutable.PriorityQueue.empty[Array[Int]]
    var currentMax = Int.MinValue
    var i = 0
    while (i < nums.size) {
      val value = nums(i).head
      heap.enqueue(Array(value, i, 0))
      currentMax = math.max(currentMax, value)
      i += 1
    }
    var bestLeft = heap.head(0)
    var bestRight = currentMax
    var done = false
    while (!done) {
      val top = heap.dequeue()
      val value = top(0)
      val listIndex = top(1)
      val index = top(2)
      if (currentMax - value < bestRight - bestLeft) {
        bestLeft = value
        bestRight = currentMax
      }
      if (index + 1 == nums(listIndex).size) {
        done = true
      } else {
        val nxt = nums(listIndex)(index + 1)
        heap.enqueue(Array(nxt, listIndex, index + 1))
        currentMax = math.max(currentMax, nxt)
      }
    }
    Array(bestLeft, bestRight)
  }
}
