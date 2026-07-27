// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

import scala.collection.mutable

object Solution {
  def furthestBuilding(heights: Array[Int], bricks: Int, ladders: Int): Int = {
    val climbs = mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    var remain = bricks
    for (i <- 0 until heights.length - 1) {
      val d = heights(i + 1) - heights(i)
      if (d > 0) {
        climbs.enqueue(d)
        if (climbs.size > ladders) remain -= climbs.dequeue()
        if (remain < 0) return i
      }
    }
    heights.length - 1
  }
}
