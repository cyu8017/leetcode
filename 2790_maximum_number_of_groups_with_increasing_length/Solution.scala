// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

object Solution {
  def maxIncreasingGroups(usageLimits: List[Int]): Int = {
    val arr = usageLimits.toArray.sorted
    var ans = 0
    var sum = 0L
    arr.foreach { v =>
      sum += v
      val need = (ans + 1L) * (ans + 2) / 2
      if (sum >= need) ans += 1
    }
    ans
  }
}
