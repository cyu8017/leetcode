// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/


class Solution {
    fun maxVacationDays(flights: Array<IntArray>, days: Array<IntArray>): Int {
        val cities = flights.size
        val weeks = days[0].size
        val NEG = -1_000_000_000
        var dp = IntArray(cities) { NEG }
        dp[0] = 0
        for (week in 0 until weeks) {
            val nxt = IntArray(cities) { NEG }
            for (city in 0 until cities) {
                if (dp[city] == NEG) continue
                for (dest in 0 until cities) {
                    if (dest == city || flights[city][dest] == 1) {
                        nxt[dest] = maxOf(nxt[dest], dp[city] + days[dest][week])
                    }
                }
            }
            dp = nxt
        }
        return dp.maxOrNull() ?: NEG
    }
}
