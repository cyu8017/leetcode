// LeetCode 3122 - Minimum Number of Operations to Satisfy Conditions
// https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

class Solution {
    fun minimumOperations(grid: Array<IntArray>): Int {
        var m = grid.size
        var n = grid[0].size
        val INF = 1  shl  29
        var f = Array(n) { IntArray(10) }
        for (row in f) { row.fill(INF) }
        for (i in 0 until n) {
            var cnt = IntArray(10)
            for (j in 0 until m) { cnt[grid[j][i]]++ }
            if (i == 0) {
                for (j in 0 until 10) { f[i][j] = m - cnt[j] }
            } else {
                for (j in 0 until 10) {
                    for (k in 0 until 10) {
                        if (j != k) f[i][j] = minOf(f[i][j], f[i - 1][k] + m - cnt[j])
                    }
                }
            }
        }
        var ans = INF
        for (j in 0 until 10) { ans = minOf(ans, f[n - 1][j]) }
        return ans
    }
}
