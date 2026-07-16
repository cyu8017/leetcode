// LeetCode 0057 - Insert Interval
// https://leetcode.com/problems/insert-interval/

object Solution {
  def insert(intervals: Array[Array[Int]], newInterval: Array[Int]): Array[Array[Int]] = {
    val result = scala.collection.mutable.ListBuffer[Array[Int]]()
    var i = 0
    var merged = newInterval.clone()

    while (i < intervals.length && intervals(i)(1) < merged(0)) {
      result += intervals(i)
      i += 1
    }

    while (i < intervals.length && intervals(i)(0) <= merged(1)) {
      merged(0) = math.min(merged(0), intervals(i)(0))
      merged(1) = math.max(merged(1), intervals(i)(1))
      i += 1
    }

    result += merged

    while (i < intervals.length) {
      result += intervals(i)
      i += 1
    }

    result.toArray
  }
}
