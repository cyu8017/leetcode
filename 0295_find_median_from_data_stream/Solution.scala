// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

import scala.collection.mutable

class MedianFinder {
  private val small = mutable.PriorityQueue.empty[Int]
  private val large = mutable.PriorityQueue.empty[Int](Ordering.Int.reverse)

  def addNum(num: Int): Unit = {
    small.enqueue(num)
    large.enqueue(small.dequeue())
    if (large.size > small.size) {
      small.enqueue(large.dequeue())
    }
  }

  def findMedian(): Double = {
    if (small.size > large.size) {
      small.head.toDouble
    } else {
      (small.head + large.head) / 2.0
    }
  }
}
