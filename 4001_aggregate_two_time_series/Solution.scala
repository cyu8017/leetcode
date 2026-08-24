// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

import scala.collection.mutable

object Solution {
  def aggregateTimeSeries(series1: Array[Array[Int]], series2: Array[Array[Int]]): Array[Array[Int]] = {
    val m = series1.length
    val n = series2.length
    var i = 0
    var j = 0
    val ans = mutable.ArrayBuffer.empty[Array[Int]]
    while (i < m && j < n) {
      val t1 = series1(i)(0)
      val v1 = series1(i)(1)
      val t2 = series2(j)(0)
      val v2 = series2(j)(1)
      if (t1 == t2) {
        ans += Array(t1, v1 + v2)
        i += 1
        j += 1
      } else if (t1 < t2) {
        ans += Array(t1, v1 + v2)
        i += 1
      } else {
        ans += Array(t2, v1 + v2)
        j += 1
      }
    }
    while (i < m) {
      ans += Array(series1(i)(0), series1(i)(1))
      i += 1
    }
    while (j < n) {
      ans += Array(series2(j)(0), series2(j)(1))
      j += 1
    }
    ans.toArray
  }
}
