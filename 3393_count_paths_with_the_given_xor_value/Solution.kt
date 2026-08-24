// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

class Solution {
    fun countPathsWithXorValue(grid: Array<IntArray>, k: Int): Int {
        val mod = 1000000007
        val m = grid.size
        val n = grid[0].size
        val dp = Array(m) { Array(n) { IntArray(16) } }
        dp[0][0][grid[0][0]] = 1
        for (i in 0 until m) {
            for (j in 0 until n) {
                for (x in 0 until 16) {
                    if (dp[i][j][x] == 0) continue
                    if (i + 1 < m) {
                        val nx = x xor grid[i + 1][j]
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod
                    }
                    if (j + 1 < n) {
                        val nx = x xor grid[i][j + 1]
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod
                    }
                }
            }
        }
        return dp[m - 1][n - 1][k]
    }
}
