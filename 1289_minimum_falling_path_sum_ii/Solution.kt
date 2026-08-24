// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution {
    fun minFallingPathSum(grid: Array<IntArray>): Int {
        var dp = grid[0].copyOf()
        for (rowIndex in 1 until grid.size) {
            val row = grid[rowIndex]
            var first = 0
            for (i in 1 until dp.size) if (dp[i] < dp[first]) first = i
            var secondValue = Int.MAX_VALUE
            for (i in dp.indices) if (i != first) secondValue = minOf(secondValue, dp[i])
            if (dp.size == 1) secondValue = 0
            val next = IntArray(dp.size)
            for (i in row.indices) {
                next[i] = row[i] + if (i == first) secondValue else dp[first]
            }
            dp = next
        }
        return dp.minOrNull()!!
    }
}
