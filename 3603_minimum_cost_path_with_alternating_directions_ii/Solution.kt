// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

class Solution {
    fun entry(i: Int, j: Int): Long { return 1L * (i + 1) * (j + 1) }

    fun minCost(m: Int, n: Int, waitCost: Array<IntArray>): Long {
        var INF = Long.MAX_VALUE / 4
        var dp = Array(m) { LongArray(n) }
        for (row in dp) { java.util.row.fill(INF) }
        dp[0][0] = entry(0, 0)
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue
                if (i > 0) {
                    var cand = dp[i - 1][j] + entry(i, j)
                    if (!(i - 1 == 0 && j == 0)) cand += waitCost[i - 1][j]
                    dp[i][j] = minOf(dp[i][j], cand)
                }
                if (j > 0) {
                    var cand = dp[i][j - 1] + entry(i, j)
                    if (!(i == 0 && j - 1 == 0)) cand += waitCost[i][j - 1]
                    dp[i][j] = minOf(dp[i][j], cand)
                }
            }
        }
        return dp[m - 1][n - 1]
    }
}
