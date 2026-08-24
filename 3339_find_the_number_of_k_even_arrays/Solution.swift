// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

class Solution {
    func countOfArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let even = m / 2, odd = m - even
        var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: 2), count: k + 1), count: n + 1)
        dp[1][0][0] = odd
        dp[1][0][1] = even
        if n >= 2 {
            for i in 1..<n {
                for j in 0...k {
                    dp[i + 1][j][0] = (dp[i + 1][j][0] + ((dp[i][j][0] + dp[i][j][1]) % mod) * odd % mod) % mod
                    dp[i + 1][j][1] = (dp[i + 1][j][1] + dp[i][j][0] * even % mod) % mod
                    if j < k {
                        dp[i + 1][j + 1][1] = (dp[i + 1][j + 1][1] + dp[i][j][1] * even % mod) % mod
                    }
                }
            }
        }
        return (dp[n][k][0] + dp[n][k][1]) % mod
    }
}
