// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

class Solution {
    fun minPathCost(grid: Array<IntArray>, moveCost: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var dp = grid[0].copyOf()
        for (r in 0 until m - 1) {
            val next = IntArray(n) { Int.MAX_VALUE / 2 }
            for (c in 0 until n) {
                val from = grid[r][c]
                for (nc in 0 until n) {
                    next[nc] = minOf(next[nc], dp[c] + moveCost[from][nc] + grid[r + 1][nc])
                }
            }
            dp = next
        }
        return dp.min()
    }
}
