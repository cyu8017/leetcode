// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

class Solution {
    fun paintWalls(cost: IntArray, time: IntArray): Int {
        var n = cost.size
        val INF = 1L  shl  60
        var dp = LongArray(n + 1)
        for (i in 1 ..n) { dp[i] = INF }
        for (i in 0 until n) {
            for (j in n downTo 0) {
                var nj = minOf(n, j + time[i] + 1)
                if (dp[j] + cost[i] < dp[nj]) dp[nj] = dp[j] + cost[i]
            }
        }
        return dp[n]
    }
}
