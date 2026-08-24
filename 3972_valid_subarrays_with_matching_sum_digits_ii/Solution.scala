// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

import scala.collection.mutable

object Solution {
  def countValidSubarrays(nums: Array[Int], x: Int): Long = {
    val byRemainder = Array.fill(10)(mutable.ArrayBuffer.empty[Long])
    byRemainder(0) += 0L
    var prefix = 0L
    var answer = 0L
    for (value <- nums) {
      prefix += value
      val required = ((prefix - x) % 10 + 10).toInt % 10
      val values = byRemainder(required)
      var power = 1L
      var more = true
      while (more && x.toLong * power <= prefix) {
        val low = x.toLong * power
        val high = (x + 1).toLong * power - 1
        val minPrefix = prefix - high
        val maxPrefix = prefix - low
        val left = lowerBound(values, minPrefix)
        val right = upperBound(values, maxPrefix)
        answer += right - left
        if (power > prefix / 10) more = false
        else power *= 10
      }
      byRemainder((prefix % 10).toInt) += prefix
    }
    answer
  }

  private def lowerBound(a: mutable.ArrayBuffer[Long], x: Long): Int = {
    var lo = 0
    var hi = a.size
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }

  private def upperBound(a: mutable.ArrayBuffer[Long], x: Long): Int = {
    var lo = 0
    var hi = a.size
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) <= x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
