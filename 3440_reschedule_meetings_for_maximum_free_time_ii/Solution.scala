// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

object Solution {
  def maxFreeTime(eventTime: Int, startTime: Array[Int], endTime: Array[Int]): Int = {
    val n = startTime.length
    val gaps = new Array[Int](n + 1)
    gaps(0) = startTime(0)
    var i = 1
    while (i < n) {
      gaps(i) = startTime(i) - endTime(i - 1)
      i += 1
    }
    gaps(n) = eventTime - endTime(n - 1)
    var ans = 0
    gaps.foreach { g => if (g > ans) ans = g }
    val leftMax = new Array[Int](n + 1)
    val rightMax = new Array[Int](n + 1)
    i = 0
    while (i <= n) {
      leftMax(i) = gaps(i)
      if (i > 0 && leftMax(i - 1) > leftMax(i)) leftMax(i) = leftMax(i - 1)
      i += 1
    }
    i = n
    while (i >= 0) {
      rightMax(i) = gaps(i)
      if (i < n && rightMax(i + 1) > rightMax(i)) rightMax(i) = rightMax(i + 1)
      i -= 1
    }
    i = 0
    while (i < n) {
      val dur = endTime(i) - startTime(i)
      val merged = gaps(i) + gaps(i + 1)
      var bestOther = 0
      if (i > 0 && leftMax(i - 1) > bestOther) bestOther = leftMax(i - 1)
      if (i + 2 <= n && rightMax(i + 2) > bestOther) bestOther = rightMax(i + 2)
      var cand = merged
      if (bestOther >= dur) cand = merged + dur
      if (cand > ans) ans = cand
      i += 1
    }
    ans
  }
}
