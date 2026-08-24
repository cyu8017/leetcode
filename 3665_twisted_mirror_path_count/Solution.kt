// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

class Solution {
    private var m: Int = 0
    private var n: Int = 0
    private var grid: Array<IntArray>? = null

    private fun nextCell(i: Int, j: Int, di: Int, dj: Int): IntArray {
        var ni = i + di
        var nj = j + dj
        while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1) {
            if (dj == 1) {
                di = 1
                dj = 0
            } else {
                di = 0
                dj = 1
            }
            ni += di
            nj += dj
        }
        if (ni < 0 || nj < 0 || ni >= m || nj >= n) return null
        return intArrayOf(ni, nj)
    }

    fun uniquePaths(grid: Array<IntArray>): Int {
        val MOD = 1_000_000_007
        this.grid = grid
        m = grid.size
        n = grid[0].size
        var dp = Array(m) { IntArray(n) }
        if (grid[0][0] == 1) return 0
        dp[0][0] = 1
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] == 1 || dp[i][j] == 0) continue
                var a = nextCell(i, j, 0, 1)
                if (a != null) dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % MOD
                var b = nextCell(i, j, 1, 0)
                if (b != null) dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % MOD
            }
        }
        return dp[m - 1][n - 1]
    }
}
