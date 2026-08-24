// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

object Solution {
  def minConnectedGroups(intervals: Array[Array[Int]], k: Int): Int = {
    val sorted = intervals.sortBy(_(0))
    val merged = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (it <- sorted) {
      if (merged.isEmpty || it(0) > merged.last(1)) merged += Array(it(0), it(1))
      else if (it(1) > merged.last(1)) merged.last(1) = it(1)
    }
    val m = merged.length
    var ans = m
    var i = 0
    while (i < m) {
      val end = merged(i)(1) + k
      var j = i
      while (j < m && merged(j)(0) <= end) j += 1
      val groups = i + 1 + (m - j)
      if (groups < ans) ans = groups
      i += 1
    }
    ans
  }
}
