// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

class Solution {
    fun maximalSquare(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty()) {
            return 0
        }
        val rows = matrix.size
        val cols = matrix[0].size
        val dp = IntArray(cols + 1)
        var maxSide = 0
        var prev = 0
        for (row in 1..rows) {
            for (col in 1..cols) {
                val temp = dp[col]
                if (matrix[row - 1][col - 1] == '1') {
                    dp[col] = minOf(dp[col], dp[col - 1], prev) + 1
                    maxSide = maxOf(maxSide, dp[col])
                } else {
                    dp[col] = 0
                }
                prev = temp
            }
        }
        return maxSide * maxSide
    }
}
