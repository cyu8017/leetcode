// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

import scala.collection.mutable

object Solution {
  def getSkyline(buildings: Array[Array[Int]]): List[List[Int]] = {
    val events = mutable.ArrayBuffer.empty[(Int, Int, Int)]
    for (building <- buildings) {
      events += ((building(0), -building(2), building(1)))
      events += ((building(1), 0, 0))
    }
    events.sortBy(event => (event._1, event._2))

    val result = mutable.ListBuffer.empty[List[Int]]
    val live = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by((item: (Int, Int)) => -item._1))
    live.enqueue((0, Int.MaxValue))

    for ((x, negH, end) <- events) {
      while (live.head._2 <= x) {
        live.dequeue()
      }
      if (negH != 0) {
        live.enqueue((negH, end))
      }
      val height = -live.head._1
      if (result.isEmpty || result.last(1) != height) {
        result += List(x, height)
      }
    }
    result.toList
  }
}
