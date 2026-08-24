// LeetCode 3951 - Minimum Energy to Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

import scala.collection.mutable

object Solution {
  def minEnergy(n: Int, brightness: Int, intervals: Array[Array[Int]]): Long = {
    val sorted = intervals.sortBy(_(0))
    val merged = mutable.ArrayBuffer(Array(sorted(0)(0), sorted(0)(1)))
    var i = 1
    while (i < sorted.length) {
      val x = sorted(i)
      val last = merged(merged.size - 1)
      if (last(1) < x(0)) merged += Array(x(0), x(1))
      else if (x(1) > last(1)) last(1) = x(1)
      i += 1
    }
    var ans = 0L
    for (interval <- merged) {
      val m = interval(1) - interval(0) + 1
      ans += ((brightness + 2) / 3).toLong * m
    }
    ans
  }
}
