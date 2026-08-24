// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/


class Solution {
    fun longestLine(mat: Array<IntArray>): Int {
        if (mat.isEmpty() || mat[0].isEmpty()) return 0
        val rows = mat.size
        val cols = mat[0].size
        val dp = Array(rows) { Array(cols) { IntArray(4) } }
        var best = 0
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (mat[r][c] == 0) continue
                dp[r][c][0] = (if (c > 0) dp[r][c - 1][0] else 0) + 1
                dp[r][c][1] = (if (r > 0) dp[r - 1][c][1] else 0) + 1
                dp[r][c][2] = (if (r > 0 && c > 0) dp[r - 1][c - 1][2] else 0) + 1
                dp[r][c][3] = (if (r > 0 && c + 1 < cols) dp[r - 1][c + 1][3] else 0) + 1
                for (d in 0 until 4) best = maxOf(best, dp[r][c][d])
            }
        }
        return best
    }
}
