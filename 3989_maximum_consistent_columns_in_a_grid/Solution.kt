// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

class Solution {
    fun maxConsistentColumns(grid: Array<IntArray>, limit: Int): Int {
        var m = grid.size
        var n = grid[0].size
        var dp = IntArray(n)
        var ans = 1
        for (j in 0 until n) {
            dp[j] = 1
            for (i in 0 until j) {
                if (dp[i] + 1 <= dp[j]) continue
                var ok = true
                for (r in 0 until m) {
                    var d = kotlin.math.abs(grid[r][j] - grid[r][i])
                    if (d > limit) { ok = false; break; }
                }
                if (ok) dp[j] = dp[i] + 1
            }
            if (dp[j] > ans) ans = dp[j]
        }
        return ans
    }
}
