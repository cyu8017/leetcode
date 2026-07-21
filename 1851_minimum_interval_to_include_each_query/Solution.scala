// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

import scala.collection.mutable

object Solution {
  def minInterval(intervals: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
    val sorted = intervals.sortBy(_(0))
    val indexed = queries.zipWithIndex.sortBy(_._1)
    val heap = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](-_._1))
    val answer = Array.fill(queries.length)(-1)
    var intervalIdx = 0

    for ((query, queryIdx) <- indexed) {
      while (intervalIdx < sorted.length && sorted(intervalIdx)(0) <= query) {
        val left = sorted(intervalIdx)(0)
        val right = sorted(intervalIdx)(1)
        heap.enqueue((right - left + 1, right))
        intervalIdx += 1
      }
      while (heap.nonEmpty && heap.head._2 < query) {
        heap.dequeue()
      }
      if (heap.nonEmpty) {
        answer(queryIdx) = heap.head._1
      }
    }
    answer
  }
}
