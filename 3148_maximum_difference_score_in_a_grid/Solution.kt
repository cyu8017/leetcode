// LeetCode 3148 - Maximum Difference Score in a Grid
// https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution {
    fun maxScore(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        val INF = 1  shl  30
        var f = Array(m) { IntArray(n) }
        var ans = -INF
        for (i in 0 until m) {
            for (j in 0 until n) {
                var x = grid[i][j]
                var mi = INF
                if (i > 0) mi = minOf(mi, f[i - 1][j])
                if (j > 0) mi = minOf(mi, f[i][j - 1])
                ans = maxOf(ans, x - mi)
                f[i][j] = minOf(x, mi)
            }
        }
        return ans
    }
}
