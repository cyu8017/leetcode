// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

object Solution {
  def employeeFreeTime(schedule: Array[Array[Array[Int]]]): Array[Array[Int]] = {
    val intervals = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (employee <- schedule; item <- employee) intervals += Array(item(0), item(1))
    val sorted = intervals.sortBy(_(0))
    val merged = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (iv <- sorted) {
      if (merged.isEmpty || merged.last(1) < iv(0)) merged += iv
      else merged.last(1) = math.max(merged.last(1), iv(1))
    }
    val result = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 1
    while (i < merged.length) {
      result += Array(merged(i - 1)(1), merged(i)(0))
      i += 1
    }
    result.toArray
  }
}
