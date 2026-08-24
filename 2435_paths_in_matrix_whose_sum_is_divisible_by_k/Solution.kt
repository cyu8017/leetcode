// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

class Solution {
    fun numberOfPaths(grid: Array<IntArray>, k: Int): Int {
            var mod: Int = 1000000007
            var m: Int = grid.size
            var n: Int = grid[0].size
            var dp: Array<Array<IntArray>> = Array(m) { Array(n) { IntArray(k) } }
            dp[0][0][grid[0][0] % k] = 1
            var i: Int = 0
    while (i < m) {
    
                var j: Int = 0
while (j < n) {

                    var r: Int = 0
while (r < k) {

                        if (dp[i][j][r] == 0) continue
                        if (i + 1 < m) {
                            var nr: Int = (r + grid[i + 1][j]) % k
                            dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod
                        }
                        if (j + 1 < n) {
                            var nr: Int = (r + grid[i][j + 1]) % k
                            dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod
                        }
r = r + 1
}
j = j + 1
}
    
    i = i + 1
    }
            return dp[m - 1][n - 1][0]
    }
}
