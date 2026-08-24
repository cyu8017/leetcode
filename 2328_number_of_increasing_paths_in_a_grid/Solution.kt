// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution {
    private val MOD = 1_000_000_007
    private lateinit var grid: Array<IntArray>
    private lateinit var dp: Array<IntArray>
    private var m = 0
    private var n = 0
    private val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))

    fun countPaths(grid: Array<IntArray>): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        dp = Array(m) { IntArray(n) }
        var ans = 0
        for (i in 0 until m) for (j in 0 until n) ans = (ans + dfs(i, j)) % MOD
        return ans
    }

    private fun dfs(r: Int, c: Int): Int {
        if (dp[r][c] != 0) return dp[r][c]
        var res = 1
        for (d in dirs) {
            val nr = r + d[0]
            val nc = c + d[1]
            if (nr in 0 until m && nc in 0 until n && grid[nr][nc] > grid[r][c]) {
                res = (res + dfs(nr, nc)) % MOD
            }
        }
        dp[r][c] = res
        return res
    }
}
