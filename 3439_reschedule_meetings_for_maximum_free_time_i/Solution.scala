// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

object Solution {
  def maxFreeTime(eventTime: Int, k: Int, startTime: Array[Int], endTime: Array[Int]): Int = {
    val n = startTime.length
    val gaps = new Array[Int](n + 1)
    gaps(0) = startTime(0)
    var i = 1
    while (i < n) {
      gaps(i) = startTime(i) - endTime(i - 1)
      i += 1
    }
    gaps(n) = eventTime - endTime(n - 1)
    val window = k + 1
    var sum = 0
    i = 0
    while (i < window && i < gaps.length) {
      sum += gaps(i)
      i += 1
    }
    var ans = sum
    i = window
    while (i < gaps.length) {
      sum += gaps(i) - gaps(i - window)
      if (sum > ans) ans = sum
      i += 1
    }
    ans
  }
}
