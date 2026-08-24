// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

object Solution {
  def mincostTickets(days: Array[Int], costs: Array[Int]): Int = {
    val dayset = days.toSet
    val last = days.last
    val dp = Array.ofDim[Int](last + 1)
    var d = 1
    while (d <= last) {
      if (!dayset.contains(d)) dp(d) = dp(d - 1)
      else {
        dp(d) = math.min(dp(d - 1) + costs(0),
          math.min(dp(math.max(0, d - 7)) + costs(1), dp(math.max(0, d - 30)) + costs(2)))
      }
      d += 1
    }
    dp(last)
  }
}
