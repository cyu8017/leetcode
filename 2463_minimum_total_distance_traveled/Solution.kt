// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution {
    fun minimumTotalDistance(robot: List<Int>, factory: Array<IntArray>): Long {
        val robots = robot.sorted()
        factory.sortBy { it[0] }
        val m = robots.size
        val pos = ArrayList<Int>()
        for (f in factory) repeat(f[1]) { pos.add(f[0]) }
        val n = pos.size
        val INF = 1L shl 60
        val dp = Array(m + 1) { LongArray(n + 1) { INF } }
        for (j in 0..n) dp[0][j] = 0
        for (i in 1..m) {
            for (j in i..n) {
                dp[i][j] = dp[i][j - 1]
                val diff = kotlin.math.abs(robots[i - 1] - pos[j - 1]).toLong()
                if (dp[i - 1][j - 1] + diff < dp[i][j]) dp[i][j] = dp[i - 1][j - 1] + diff
            }
        }
        return dp[m][n]
    }
}
