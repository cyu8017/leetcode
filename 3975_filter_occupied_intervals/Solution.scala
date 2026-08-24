// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

import scala.collection.mutable

object Solution {
  def filterOccupiedIntervals(occupiedIntervals: Array[Array[Int]], freeStart: Int, freeEnd: Int): Array[Array[Int]] = {
    val sorted = occupiedIntervals.sortBy(_(0))
    val busy = mutable.ArrayBuffer(Array(sorted(0)(0), sorted(0)(1)))
    var i = 1
    while (i < sorted.length) {
      val cur = sorted(i)
      val last = busy(busy.size - 1)
      if (last(1) + 1 < cur(0)) busy += Array(cur(0), cur(1))
      else if (cur(1) > last(1)) last(1) = cur(1)
      i += 1
    }
    val ans = mutable.ArrayBuffer.empty[Array[Int]]
    for (it <- busy) {
      val s = it(0)
      val e = it(1)
      if (e < freeStart || s > freeEnd) ans += Array(s, e)
      else {
        if (s < freeStart) ans += Array(s, freeStart - 1)
        if (e > freeEnd) ans += Array(freeEnd + 1, e)
      }
    }
    ans.toArray
  }
}
