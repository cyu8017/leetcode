// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

class Solution {
    func maximumAmount(_ coins: [[Int]]) -> Int {
        let m = coins.count, n = coins[0].count
        let neg = -(1 << 30)
        var dp = Array(repeating: Array(repeating: Array(repeating: neg, count: 3), count: n), count: m)
        if coins[0][0] < 0 {
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0
            dp[0][0][2] = 0
        } else {
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = coins[0][0]
            dp[0][0][2] = coins[0][0]
        }
        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }
                for k in 0..<3 {
                    var best = neg
                    if i > 0 { best = max(best, dp[i - 1][j][k]) }
                    if j > 0 { best = max(best, dp[i][j - 1][k]) }
                    if best == neg { continue }
                    if coins[i][j] >= 0 { dp[i][j][k] = best + coins[i][j] }
                    else { dp[i][j][k] = max(dp[i][j][k], best + coins[i][j]) }
                }
                for k in 1..<3 {
                    var best = neg
                    if i > 0 { best = max(best, dp[i - 1][j][k - 1]) }
                    if j > 0 { best = max(best, dp[i][j - 1][k - 1]) }
                    if best != neg && coins[i][j] < 0 { dp[i][j][k] = max(dp[i][j][k], best) }
                }
            }
        }
        return max(dp[m - 1][n - 1][0], max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]))
    }
}
