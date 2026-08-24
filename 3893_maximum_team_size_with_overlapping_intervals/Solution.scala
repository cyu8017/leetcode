// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

object Solution {
  def maximumTeamSize(startTime: Array[Int], endTime: Array[Int]): Int = {
    val n = startTime.length
    val st = startTime.clone()
    val en = endTime.clone()
    java.util.Arrays.sort(st)
    java.util.Arrays.sort(en)
    var ans = 0
    var t = 0
    while (t < n) {
      val l = startTime(t)
      val r = endTime(t)
      val i = upperBound(en, l - 1)
      val j = upperBound(st, r)
      ans = math.max(ans, j - i)
      t += 1
    }
    ans
  }

  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
