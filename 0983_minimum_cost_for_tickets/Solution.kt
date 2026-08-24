// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution {
    fun mincostTickets(days: IntArray, costs: IntArray): Int {
        val dayset = HashSet<Int>()
        for (d in days) dayset.add(d)
        val last = days[days.size - 1]
        val dp = IntArray(last + 1)
        for (d in 1..last) {
            if (!dayset.contains(d)) {
                dp[d] = dp[d - 1]
            } else {
                dp[d] = minOf(
                    dp[d - 1] + costs[0],
                    minOf(dp[maxOf(0, d - 7)] + costs[1], dp[maxOf(0, d - 30)] + costs[2])
                )
            }
        }
        return dp[last]
    }
}
