// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

object Solution {
  def merge(intervals: Array[Array[Int]]): Array[Array[Int]] = {
    val sorted = intervals.sortBy(_(0))
    val merged = scala.collection.mutable.ListBuffer(sorted.head)

    sorted.tail.foreach { current =>
      val last = merged.last
      if (current(0) <= last(1)) {
        merged(merged.length - 1) = Array(last(0), math.max(last(1), current(1)))
      } else {
        merged += current
      }
    }

    merged.toArray
  }
}
