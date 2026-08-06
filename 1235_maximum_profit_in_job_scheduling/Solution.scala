// LeetCode 1235 - Maximum Profit in Job Scheduling
// https://leetcode.com/problems/maximum-profit-in-job-scheduling/

object Solution {
  def jobScheduling(startTime: Array[Int], endTime: Array[Int], profit: Array[Int]): Int = {
    val jobs = endTime.indices.map(i => (endTime(i), startTime(i), profit(i))).sortBy(_._1)
    val ends = scala.collection.mutable.ArrayBuffer(0)
    val dp = scala.collection.mutable.ArrayBuffer(0)
    for ((end, start, gain) <- jobs) {
      var lo = 0
      var hi = ends.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (ends(mid) <= start) lo = mid + 1 else hi = mid
      }
      val i = lo - 1
      ends += end
      dp += math.max(dp.last, dp(i) + gain)
    }
    dp.last
  }
}
