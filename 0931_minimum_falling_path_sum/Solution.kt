// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

class Solution {
    fun minFallingPathSum(matrix: Array<IntArray>): Int {
        var dp = matrix[0].copyOf()
        for (r in 1 until matrix.size) {
            var ndp = IntArray(dp.size)
            for (c in 0 until dp.size) {
                var best = dp[c]
                if (c > 0) best = minOf(best, dp[c - 1])
                if (c + 1 < dp.size) best = minOf(best, dp[c + 1])
                ndp[c] = matrix[r][c] + best
            }
            dp = ndp
        }
        var ans = dp[0]
        for (x in dp) { ans = minOf(ans, x); }
        return ans
    }
}
