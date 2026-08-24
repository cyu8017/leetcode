// LeetCode 3956 - Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/

import scala.collection.mutable

object Solution {
  def maxSum(nums: Array[Int], m: Int, l: Int, r: Int): Long = {
    val n = nums.length
    val prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    var dp = new Array[Long](n + 1)
    var bestSelected = -(1L << 62)
    var count = 1
    while (count <= m) {
      val next = dp.clone()
      val deque = mutable.ArrayBuffer.empty[Int]
      var end = 1
      while (end <= n) {
        val addIndex = end - l
        if (addIndex >= 0) {
          val value = dp(addIndex) - prefix(addIndex)
          var keep = true
          while (deque.nonEmpty && keep) {
            val last = deque(deque.size - 1)
            if (dp(last) - prefix(last) > value) keep = false
            else deque.remove(deque.size - 1)
          }
          deque += addIndex
        }
        val minIndex = end - r
        while (deque.nonEmpty && deque(0) < minIndex) deque.remove(0)
        if (deque.nonEmpty) {
          val candidate = prefix(end) + dp(deque(0)) - prefix(deque(0))
          if (candidate > next(end)) next(end) = candidate
          if (candidate > bestSelected) bestSelected = candidate
        }
        if (next(end - 1) > next(end)) next(end) = next(end - 1)
        end += 1
      }
      dp = next
      count += 1
    }
    bestSelected
  }
}
