// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

class Solution {
    func countPathsWithXorValue(_ grid: [[Int]], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let m = grid.count, n = grid[0].count
        let XOR = 16
        if k >= XOR { return 0 }
        var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: XOR), count: n), count: m)
        dp[0][0][grid[0][0]] = 1
        for i in 0..<m {
            for j in 0..<n {
                for x in 0..<XOR {
                    if dp[i][j][x] == 0 { continue }
                    if i + 1 < m {
                        let nx = x ^ grid[i + 1][j]
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod
                    }
                    if j + 1 < n {
                        let nx = x ^ grid[i][j + 1]
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod
                    }
                }
            }
        }
        return dp[m - 1][n - 1][k]
    }
}
