// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

class Solution {
    func numberOfPaths(_ grid: [[Int]], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let m = grid.count, n = grid[0].count
        var dp = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: k), count: n), count: m)
        dp[0][0][grid[0][0] % k] = 1
        for i in 0..<m {
            for j in 0..<n {
                for r in 0..<k {
                    if dp[i][j][r] == 0 { continue }
                    if i + 1 < m {
                        let nr = (r + grid[i + 1][j]) % k
                        dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod
                    }
                    if j + 1 < n {
                        let nr = (r + grid[i][j + 1]) % k
                        dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod
                    }
                }
            }
        }
        return dp[m - 1][n - 1][0]
    }
}
