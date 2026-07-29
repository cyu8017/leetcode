// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution {
    fun minScoreTriangulation(values: IntArray): Int {
        val n = values.size
        val memo = Array(n) { IntArray(n) { -1 } }
        return dp(values, 0, n - 1, memo)
    }

    private fun dp(values: IntArray, i: Int, j: Int, memo: Array<IntArray>): Int {
        if (j - i < 2) return 0
        if (memo[i][j] != -1) return memo[i][j]
        var best = Int.MAX_VALUE
        for (k in i + 1 until j) {
            best = minOf(best, dp(values, i, k, memo) + values[i] * values[k] * values[j] + dp(values, k, j, memo))
        }
        memo[i][j] = best
        return best
    }
}
