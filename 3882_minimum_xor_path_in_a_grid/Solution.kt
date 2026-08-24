// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

class Solution {
    fun minXor(grid: Array<IntArray>): Int {
        var rows = grid.size
        var cols = grid[0].size
        var dp = BooleanArray(cols)[]
        for (i in 0 until cols) { dp[i] = BooleanArray(1024) }
        for (row in 0 until rows) {
            var left = BooleanArray(1024)
            for (col in 0 until cols) {
                var next = BooleanArray(1024)
                var value = grid[row][col]
                if (row == 0 && col == 0) {
                    next[value] = true
                } else {
                    for (xorv in 0 until 1024) {
                        if (dp[col][xorv] || left[xorv]) next[xorv ^ value] = true
                    }
                }
                dp[col] = next
                left = next
            }
        }
        for (xorv in 0 until 1024) {
            if (dp[cols - 1][xorv]) return xorv
        }
        return -1
    }
}
